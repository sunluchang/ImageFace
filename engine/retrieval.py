import pickle as pkl
import os
import cv2
import numpy as np
import torchvision
import PIL.Image
import torch
from skimage import img_as_ubyte
import torch.nn as nn

class retrieval():
    def __init__(self, dataset_root, verbose = False):
        self.dataset_root = dataset_root
        self.train_feature = self.load_train_feature()
        self.transform = self.get_transform()
        self.model = torchvision.models.vgg16(pretrained=True)
        self.feature_map = self.get_feature_map()
        self.pooling_approach = 'avg_max_pooling'
        self.verbose = verbose

    # return activation of pool5 in vgg16
    def get_feature_map(self):
        features = self.model.features
        features = torch.nn.Sequential(*list(features.children())[:-1])
        features.eval()
        return features

    # load train image SCDA_pool5 features
    def load_train_feature(self):
        path = os.path.join(self.dataset_root, 'train_features.pkl')
        with open(path, 'rb') as f:
            feature = pkl.load(f)
        return feature

    # get retrieval image SCDA_pool5
    def get_retrieval_image_feature(self, retrieval_image): # image
        with torch.no_grad():
            retrieval_image = PIL.Image.fromarray(retrieval_image)
            original_image = retrieval_image.copy()
            retrieval_image = self.transform(retrieval_image)
            retrieval_image.require_grads = False
            retrieval_image = torch.unsqueeze(retrieval_image, dim=0)
            retrieval_image_feature = self.feature_map(retrieval_image)
            retrieval_image_feature_aggre = torch.sum(retrieval_image_feature, dim=1) # sum along the channel dimension
            retrieval_image_feature_threshold = torch.mean(retrieval_image_feature_aggre, dim=(1, 2)) # the mean value of the aggregation feature map
            mask = self.get_mask(retrieval_image_feature_aggre, retrieval_image_feature_threshold)
            mask = self.get_largest_cc(mask)
            retrieval_image_feature_useful = retrieval_image_feature[:, :, mask==1]

            if self.pooling_approach == 'average_pooling':
                feature_vector = torch.mean(retrieval_image_feature_useful, dim=2)
            elif self.pooling_approach == 'max_pooling':
                feature_vector = torch.max(retrieval_image_feature_useful, dim=2)
            elif self.pooling_approach == 'avg_max_pooling':
                feature_vector_mean = torch.mean(retrieval_image_feature_useful, dim=2)  # [1, 512]
                feature_vector_max = torch.max(retrieval_image_feature_useful, dim=2)[0]
                feature_vector = torch.cat([feature_vector_mean, feature_vector_max], dim=1)
        return feature_vector

    # data preprocessing for vgg16
    def get_transform(self):
        return torchvision.transforms.Compose([
            torchvision.transforms.ToTensor(),
            torchvision.transforms.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
        ])

    # get the mask located the main object
    def get_mask(self, feature_aggre, threshold):
        res = feature_aggre.clone()
        res[feature_aggre < threshold] = 0
        res[feature_aggre > threshold] = 1
        return res

    # return the largest connected component of mask
    def get_largest_cc(self, binary):
        binary = torch.squeeze(binary)
        binary = binary.numpy()
        binary = img_as_ubyte(binary)
        num_component, label_map = cv2.connectedComponents(binary)
        if num_component == 1:
            mask = torch.zeros(size=(448, 448))
            return mask
        pixels_per_class = np.zeros(shape=num_component - 1)
        for i in range(1, num_component - 1):
            pixels_per_class[i] = np.sum(label_map == i)#count number for rach label
        largest_label = np.argmax(pixels_per_class)
        mask = np.zeros(shape=binary.shape)
        mask[label_map == largest_label] = 1
        mask = torch.from_numpy(mask)
        return mask

    def retrival_from_image_root(self, retrieval_image_keys):
        retrieval_image_result = {}
        AP_top1_list = []
        AP_top5_list = []
        AP_top10_list = []
        AP_top50_list = []
        for i in range(len(retrieval_image_keys)):
            retrieval_image = cv2.imread(os.path.join(self.dataset_root, 'images/' + retrieval_image_keys[i]))
            retrieval_image = cv2.cvtColor(retrieval_image, cv2.COLOR_BGR2RGB)
            retrieval_image = cv2.resize(retrieval_image, dsize=(448, 448))
            retrieval_image = np.array(retrieval_image)
            retrieval_image_feature = self.get_retrieval_image_feature(retrieval_image)
            retrieval_image_feature = retrieval_image_feature.numpy()
            cos_similarity = {}
            for key in self.train_feature.keys():
                train_feature_2_norm = np.linalg.norm(self.train_feature[key][0], ord=2)
                retrieval_image_feature_2_norm = np.linalg.norm(retrieval_image_feature, ord=2)
                cos_similarity[key] = np.dot(self.train_feature[key][0], retrieval_image_feature.T) / (
                            train_feature_2_norm * retrieval_image_feature_2_norm)
            top_50_relevant = []
            prec = []
            number_TP = 0
            for j in range(50):
                max_key = max(cos_similarity, key=cos_similarity.get)  # return the key of the min value
                max_class_label = self.train_feature[max_key][1]
                top_50_relevant.append([max_key, max_class_label])
                del cos_similarity[max_key]
                if int(retrieval_image_keys[i][:3]) == max_class_label:
                    number_TP = number_TP + 1
                    prec.append(number_TP/(j + 1))
                else:
                    prec.append(0)
                if j == 0:
                    if number_TP == 0:
                        AP_top1_list.append(0)
                    else:
                        AP_top1_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 4:
                    if number_TP == 0:
                        AP_top5_list.append(0)
                    else:
                        AP_top5_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 9:
                    if number_TP == 0:
                        AP_top10_list.append(0)
                    else:
                        AP_top10_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 49:
                    if number_TP == 0:
                        AP_top50_list.append(0)
                    else:
                        AP_top50_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
            retrieval_image_result[retrieval_image_keys[i]] = top_50_relevant
        mAP = [np.mean(np.array(AP_top1_list, dtype=float)), np.mean(np.array(AP_top5_list, dtype=float)),
               np.mean(np.array(AP_top10_list, dtype=float)), np.mean(np.array(AP_top50_list, dtype=float))]
        return [retrieval_image_result, mAP]

    def cal_mAP(self):
        with open(os.path.join(self.dataset_root, 'test.pkl'), 'rb') as f:
            test_data = pkl.load(f)
        retrieval_image_result = {}
        test_data_feature = {}
        cos_similarity_test_train = {}
        AP_top1_list = []
        AP_top5_list = []
        AP_top10_list = []
        AP_top50_list = []
        flag = 0
        for key_test_data in test_data.keys():
            flag = flag + 1
            if flag == 10:
                break
            retrieval_image_feature = self.get_retrieval_image_feature(np.array(test_data[key_test_data][0]))
            retrieval_image_feature = retrieval_image_feature.numpy()
            test_data_feature[key_test_data] = retrieval_image_feature
            cos_similarity = {}
            for key_train_feature in self.train_feature.keys():
                train_feature_2_norm = np.linalg.norm(self.train_feature[key_train_feature][0], ord=2)
                retrieval_image_feature_2_norm = np.linalg.norm(retrieval_image_feature, ord=2)
                cos_similarity[key_train_feature] = np.dot(self.train_feature[key_train_feature][0], retrieval_image_feature.T) / (
                            train_feature_2_norm * retrieval_image_feature_2_norm)
            cos_similarity_test_train[key_test_data] = cos_similarity
            top_50_relevant = []
            prec = []
            number_TP = 0
            for j in range(50):
                max_key = max(cos_similarity, key=cos_similarity.get)  # return the key of the min value
                max_class_label = self.train_feature[max_key][1]
                top_50_relevant.append([max_key, max_class_label])
                del cos_similarity[max_key]
                if test_data[key_test_data][1] == max_class_label:
                    number_TP = number_TP + 1
                    prec.append(number_TP/(j + 1))
                else:
                    prec.append(0)
                if j == 0:
                    if number_TP == 0:
                        AP_top1_list.append(0)
                    else:
                        AP_top1_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 4:
                    if number_TP == 0:
                        AP_top5_list.append(0)
                    else:
                        AP_top5_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 9:
                    if number_TP == 0:
                        AP_top10_list.append(0)
                    else:
                        AP_top10_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
                if j == 49:
                    if number_TP == 0:
                        AP_top50_list.append(0)
                    else:
                        AP_top50_list.append(np.sum(np.array(prec, dtype=float)) / number_TP)
            retrieval_image_result[key_test_data] = top_50_relevant
        mAP = [np.mean(np.array(AP_top1_list, dtype=float)), np.mean(np.array(AP_top5_list, dtype=float)),
               np.mean(np.array(AP_top10_list, dtype=float)), np.mean(np.array(AP_top50_list, dtype=float))]

        # save test_data_feature
        with open(os.path.join(self.dataset_root, 'test_data_feature.pkl'), 'wb') as f:
            pkl.dump(test_data_feature, f)
        # save cosine distance
        with open(os.path.join(self.dataset_root, 'cos_similarity_test_train.pkl'), 'wb') as f:
            pkl.dump(cos_similarity_test_train, f)
        return [retrieval_image_result, mAP]
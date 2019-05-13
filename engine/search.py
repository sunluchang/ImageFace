# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
author  @   Sun Luchang
m_date  @   2019-05-05

multi threads searching for Digital-Image-Processing-HomeWork
'''

from config import _MINISIZE, _MAX_SEARCH_CLASS, _CLASS_PATH, _CLASSES, _IMG_PATH, _S_CLASSES, _D_CLASSES, SERVER_ADDR

import re
from PyQt5 import QtCore
from PIL.ImageQt import ImageQt
from PIL import Image
import os, requests, json, time

from engine.myPhoto import myPhoto, myPhoto2
from engine.retrieval import retrieval

def preReadFile():
    # run once when _CLASSES is None
    _CLASSES = []
    f = open(_CLASS_PATH)
    while True:
        line = f.readline()
        if line:
            __class = line.split(" ")[1][:-1]
            _CLASSES.append(__class)
        else:
            break
    print(_CLASSES)

class searchBirdByTxt(QtCore.QThread):
    SCsignal = QtCore.pyqtSignal(dict)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.keyword = ""
        self.picPath = _IMG_PATH

    def setKeyword(self, key, net=False):
        self.keyword = key
        self.network = net

    def __del__(self):
        self.wait()

    def run(self):
        # pay money for speed
        # time.sleep(1)
        # pay money for speed
        res = self.__find()

        for key in res.keys():
            fullPath = os.path.join(self.picPath, key)
            for _, _, files in os.walk(fullPath):
                for file in files:
                    if file[-3:] == 'jpg':
                        _imgPath = os.path.join(fullPath, file)
                        _img = Image.open( os.path.join(fullPath, file) )
                        (_w, _h) = _img.size
                        if _w > _h:
                            _h = int( 1.0*_MINISIZE/_w * _h )
                            _w = _MINISIZE
                            _img = _img.resize((_w, _h))
                        else:
                            _w = int( 1.0*_MINISIZE/_h * _w )
                            _h = _MINISIZE
                            _img = _img.resize((_w, _h))

                        _tmp = myPhoto(ImageQt(_img), _w, _h, _imgPath)
                        res[key].append(_tmp)

        self.SCsignal.emit(res)

    def __find(self):
        suggestions = {}
        pattern = '.*?'.join(self.keyword)
        regex = re.compile(pattern)

        _COUNT = 0
        for key in _CLASSES:
            if re.search(regex, key):
                suggestions[key] = []
                _COUNT += 1
                if _COUNT > _MAX_SEARCH_CLASS:
                    break

        return suggestions

class searchBirdByPic(QtCore.QThread):
    SCsignal = QtCore.pyqtSignal(dict)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.root = _IMG_PATH
        self.network = False

    def setKeyword(self, key, net=False):
        print(key)
        self.path = key
        self.network = net

    def __del__(self):
        self.wait()

    def run(self):
        # pay money for speed
        # time.sleep(2)
        # pay money for speed
        search = self._find()
        MomAndSon = search[0]       # dict { '001.class/bird.jpg': [ ['001.class/son.jpg'(str), class(int)], [], ... ]}
        mAP = search[1]             # list [1, 2, 3, 4]

        result = {}

        for key in MomAndSon.keys():
            sons = MomAndSon[key]
            mom = key.split('.')[1]
            momName = key.split('.')[0]
            result[mom] = []
            for son in sons:
                fullPath = os.path.join(self.root, son[0])
                _img = Image.open( fullPath )
                (_w, _h) = _img.size
                if _w > _h:
                    _h = int(1.0 * _MINISIZE / _w * _h)
                    _w = _MINISIZE
                    _img = _img.resize((_w, _h))
                else:
                    _w = int(1.0 * _MINISIZE / _h * _w)
                    _h = _MINISIZE
                    _img = _img.resize((_w, _h))

                _tmp = myPhoto2(ImageQt(_img), _w, _h, fullPath, momName, son[0].split('.')[0])
                result[mom].append(_tmp)

        final_result = {
            'pic': result,
            'map': mAP,
        }
        self.SCsignal.emit(final_result)

    def _dealPath(self):
        newPath = []
        for p in self.path:
            newp = p.split('images/')[1]
            newPath.append(newp)
        return newPath

    def netSearch(self, files):
        d = json.dumps({
            'data': files,
        })
        res = requests.post(SERVER_ADDR, data=d)
        res = eval(res.text)
        return eval(res['res'])

    def _find(self):
        retrieval_image_keys = self._dealPath()
        if self.network:
            return self.netSearch(retrieval_image_keys)
        dataset_root = '/Users/thatslc/Downloads/CUB_200_2011/CUB_200_2011'
        engine = retrieval(dataset_root, verbose=False)
        return engine.retrival_from_image_root(retrieval_image_keys)
        #test_data_result_mAP = retrieval_inst.cal_mAP()
        # with open(os.path.join(dataset_root, 'test_data_result_mAP.pkl'), 'wb') as f:
        # pkl.dump(test_data_result_mAP, f)


class realSearch(QtCore.QThread):
    SCsignal = QtCore.pyqtSignal(list)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.keyword = ""

    def setKeyword(self, key):
        self.keyword = key

    def __del__(self):
        self.wait()

    def run(self):
        self.SCsignal.emit(self.__find())

    def __find(self):
        suggestions = []
        pattern = '.*?'.join(self.keyword)
        regex = re.compile(pattern)

        _COUNT = 0
        for key in _S_CLASSES:
            if re.search(regex, key):
                suggestions.append(_D_CLASSES[key])
                _COUNT += 1
            if _COUNT > 5:
                break

        return suggestions

class testNet(QtCore.QThread):
    SCsignal = QtCore.pyqtSignal(int)
    def __init__(self, parent = None):
        super().__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        while 1:
            try:
                ping = requests.get(SERVER_ADDR, timeout = 5).text
                self.SCsignal.emit(1)
            except:
                self.SCsignal.emit(0)
            time.sleep(5)
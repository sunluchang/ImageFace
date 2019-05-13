from PyQt5 import QtWidgets

class myPicLabel(QtWidgets.QLabel):
    def __init__(self, img):
        super(myPicLabel, self).__init__()
        self.__raw = img
        self.__path = img.getPath()

class myPhoto:
    def __init__(self, photo, x, y, p):
        self.__photo = photo
        self.__width = x
        self.__height = y
        self.__path = p

    def getPhoto(self):
        return self.__photo

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getPath(self):
        return self.__path

    def iamTrue(self):
        return 0

class myPhoto2:
    def __init__(self, photo, x, y, p, mom, me):
        self.__photo = photo
        self.__width = x
        self.__height = y
        self.__path = p

        self.__mom = mom
        self.__me = me

    def iamTrue(self):
        if self.__mom == self.__me:
            return 1
        else:
            return 2

    def getPhoto(self):
        return self.__photo

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getPath(self):
        return self.__path

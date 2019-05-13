# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
author  @   Sun Luchang
m_date  @   2019-05-11

UI for Digital-Image-Processing-HomeWork
'''

from PyQt5 import QtWidgets, QtGui
from ui_src.ywt import Ui_MainWindow
import PIL.Image
from PIL.ImageQt import ImageQt

from config import YWTexe

import os

class ywtUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ywtUI, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(700, 480)

        self.setWindowTitle('YWT')

        self.ui.raw.setText('')
        self.ui.t1.setText('')
        self.ui.t2.setText('')
        self.ui.t3.setText('')
        self.ui.t4.setText('')

        self.path = None
        self.kersize = 1
        self.select = 0

        self.ui.pushButton.clicked.connect(self.selectFile)
        self.ui.start.clicked.connect(self.doit)

        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.ui.radioButton, 0)
        self.buttonGroup.addButton(self.ui.radioButton_2, 1)
        self.buttonGroup.addButton(self.ui.radioButton_3, 2)

        self.ui.slider.setMaximum(1)
        self.ui.slider.setMaximum(100)
        self.ui.slider.setSingleStep(1)
        self.ui.spinBox.setMaximum(1)
        self.ui.spinBox.setMaximum(100)
        self.ui.spinBox.setSingleStep(1)
        self.ui.slider.valueChanged.connect(self.ui.spinBox.setValue)
        self.ui.spinBox.valueChanged.connect(self.ui.slider.setValue)


    def setNewValue(self, res):
        self.kersize = int(res + 1)
        self.ui.lineEdit.setText(self.kersize)

    def setNewSlider(self, r):
        print(r)
        self.kersize = int(r)
        #self.ui.slider.setValue(int(r))

    def getClick(self):
        self.select = self.buttonGroup.checkedId()

    def selectFile(self):
        fileDialog = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片",
                                                            "/Users/thatslc/PycharmProjects/ImageFace/data/ywt",
                                                            ("图片文件(*.png *.jpg *.tif *.bmp)"))
        # fileDialog is a tuple ([files, ...], [format])
        if fileDialog[0] != '':
            self.path = fileDialog[0]
            self.showRaw()

    def _openIMG(self, path):
        img = PIL.Image.open(path)
        (w, h) = img.size
        if (w > h):
            h = 200 / w * h
            w = 200
        else:
            w = 200 / h * w
            h = 200
        img = img.resize((int(w), int(h)))
        return ImageQt(img)

    def doit(self):
        if not self.path:
            return

        order = "%s %s /Users/thatslc/PycharmProjects/ImageFace/data/ywt/ %d %d %d" % (YWTexe, self.path, self.select, self.kersize, self.kersize)
        res = os.system(order)

        if res == 0:
            i1 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/ywt/closeImage.bmp")
            i2 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/ywt/dilateImage.bmp")
            i3 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/ywt/erodeImage.bmp")
            i4 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/ywt/openImage.bmp")
            self.ui.t1.setPixmap(QtGui.QPixmap.fromImage(i1))
            self.ui.t2.setPixmap(QtGui.QPixmap.fromImage(i2))
            self.ui.t3.setPixmap(QtGui.QPixmap.fromImage(i3))
            self.ui.t4.setPixmap(QtGui.QPixmap.fromImage(i4))

    def showRaw(self):
        if not self.path:
            return
        img = self._openIMG(self.path)
        self.ui.raw.setPixmap(QtGui.QPixmap.fromImage(img))



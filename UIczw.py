# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
author  @   Sun Luchang
m_date  @   2019-05-11

UI for Digital-Image-Processing-HomeWork
'''

from PyQt5 import QtWidgets, QtGui
from ui_src.slc import Ui_MainWindow
import PIL.Image
from PIL.ImageQt import ImageQt

import os

from config import CZWexe

class czwUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(czwUI, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(600, 480)

        self.setWindowTitle("FFT")

        self.ui.raw.setText('')
        self.ui.a.setText('')
        self.ui.b.setText('')
        self.ui.c.setText('')

        self.path = None

        self.ui.aa.clicked.connect(self.fft)
        self.ui.aa.setText("FFT")
        self.ui.bb.close()
        self.ui.cc.close()
        self.ui.slider.close()
        self.ui.pushButton.clicked.connect(self.selectFile)

        self.ui.raw_3.setText('AMP')
        self.ui.raw_4.setText('PHASE')
        self.ui.raw_5.setText('RECOVER IMAGE')

    def selectFile(self):
        fileDialog = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片",
                                                            "/Users/thatslc/PycharmProjects/ImageFace/data/czw",
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

    def fft(self):
        if not self.path:
            return

        newp = self.path.split('.')[0]
        order = "%s --image_file_name %s --image_save_name /Users/thatslc/PycharmProjects/ImageFace/data/czw" % (CZWexe, self.path)
        res = os.system(order)

        print(order)

        if res == 0:
            try:
                img1 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/czw/amp.jpg")
                img2 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/czw/phase.jpg")
                img3 = self._openIMG("/Users/thatslc/PycharmProjects/ImageFace/data/czw/recover image.jpg")
                self.ui.a.setPixmap(QtGui.QPixmap.fromImage(img1))
                self.ui.b.setPixmap(QtGui.QPixmap.fromImage(img2))
                self.ui.c.setPixmap(QtGui.QPixmap.fromImage(img3))
            except Exception as e:
                print(e)

    def showRaw(self):
        if not self.path:
            return
        img = self._openIMG(self.path)
        self.ui.raw.setPixmap(QtGui.QPixmap.fromImage(img))



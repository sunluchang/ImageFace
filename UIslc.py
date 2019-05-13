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

from config import _SLC_EXE, _SYS_ROOT_PATH_

import os

class slcUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(slcUI, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(600, 480)

        self.setWindowTitle('FILTER')

        self.ui.raw.setText('')
        self.ui.a.setText('')
        self.ui.b.setText('')
        self.ui.c.setText('')

        self.path = None
        self.adaptivehold = 0

        self.ui.cc.clicked.connect(self.adaptive)
        self.ui.aa.clicked.connect(self.arith)
        self.ui.bb.clicked.connect(self.geo)
        self.ui.pushButton.clicked.connect(self.selectFile)

        self.ui.slider.valueChanged.connect(self.setNewValue)

    def setNewValue(self, res):
        self.adaptivehold = int(res/99.0 * 4000)
        self.ui.label.setText(str(self.adaptivehold))

    def selectFile(self):
        fileDialog = QtWidgets.QFileDialog.getOpenFileName(self, "选择图片",
                                                            _SYS_ROOT_PATH_ + "data/slc",
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

    def arith(self):
        if not self.path:
            return

        newp = self.path.split('.')[0] + "Arith.jpg"
        order = "%s %s %s %d" % (_SLC_EXE, self.path, newp, 0)
        res = os.system(order)

        if res == 0:
            img = self._openIMG(newp)
            self.ui.a.setPixmap(QtGui.QPixmap.fromImage(img))

    def geo(self):
        if not self.path:
            return

        newp = self.path.split('.')[0] + "Arith.jpg"
        order = "%s %s %s %d" % (_SLC_EXE, self.path, newp, 1)
        res = os.system(order)

        if res == 0:
            img = self._openIMG(newp)
            self.ui.b.setPixmap(QtGui.QPixmap.fromImage(img))

    def adaptive(self):
        if not self.path:
            return

        newp = self.path.split('.')[0] + "Arith.jpg"
        order = "%s %s %s %d %d" % (_SLC_EXE, self.path, newp, 2, self.adaptivehold)
        res = os.system(order)

        if res == 0:
            img = self._openIMG(newp)
            self.ui.c.setPixmap(QtGui.QPixmap.fromImage(img))

    def showRaw(self):
        if not self.path:
            return
        img = self._openIMG(self.path)
        self.ui.raw.setPixmap(QtGui.QPixmap.fromImage(img))



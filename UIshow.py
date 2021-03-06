# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
author  @   Sun Luchang
m_date  @   2019-05-06

UI for Digital-Image-Processing-HomeWork
'''

import datetime

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from ui_src.showUI import Ui_showUI

from engine.search import searchBirdByPic, searchBirdByTxt
from engine.myPhoto import myPicLabel

from config import _LINE_PIC_NUM, _MINI_POS_SIZE, _MINISIZE, rightStyle, wrongStyle, normalStyle

class showUI(QtWidgets.QMainWindow):
    def __init__(self, net=False, parent=None):
        super(showUI, self).__init__(parent)
        self.ui = Ui_showUI()
        self.ui.setupUi(self)
        self.setFixedSize(1000, 700)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.photoData = None
        self.picSearchState = False
        self.hasData = False
        self.network = net

        # 设置 QListWidget 的属性
        self.ui.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.ui.listWidget.setMovement(QtWidgets.QListView.Static)
        self.ui.listWidget.setSpacing(5)
        self.ui.listWidget.clicked.connect(self.changeIndex)
        # 设置 QListWidget 的属性

        self.ui.rightNUM.setStyleSheet("color: rgb(10, 222, 10);")
        self.ui.wrongNUM.setStyleSheet("color: rgb(200, 10, 10);")

        self.searchThreadTXT = searchBirdByTxt()
        self.searchThreadTXT.SCsignal.connect(self.showResult)

        self.mutex = QtCore.QMutex

    def _showEmpty(self):
        print("THERE ARE NOTHING.")

    def _showPic(self, pics):
        if self.picSearchState:
            self.photoData = pics['pic']
            self.mAP = pics['map']
            self.hasData = True
            self.photoDataKeys = list(self.photoData.keys())
            self.__showTab(0)
        else:
            classes = list(pics.keys())
            self.setFather(classes)
            self.photoData = pics
            self.photoDataKeys = classes
            self.__showTab(0)

    def changeIndex(self, index):
        if not self.hasData and self.picSearchState:
            return
        try:
            self.__showTab(self.ui.listWidget.currentRow())
        except:
            pass

    def __showTab(self, index):
        photos = self.photoData[self.photoDataKeys[index]]

        length = len(photos)
        if length % _LINE_PIC_NUM != 0:
            length = (int(length / _LINE_PIC_NUM) + 1) * _MINI_POS_SIZE
        else:
            length = (length / _LINE_PIC_NUM) * _MINI_POS_SIZE

        rightNUM = 0
        wrongNUM = 0

        scrollAreaWidgetContents = QtWidgets.QWidget()
        scrollAreaWidgetContents.setMinimumSize(800, length)
        scrollAreaWidgetContents.setGeometry(200, 100, 810, 500)

        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setWidget(scrollAreaWidgetContents)
        scrollArea.setAutoFillBackground(True)
        scrollArea.setWidgetResizable(True)

        scrollArea.setGeometry(200, 110, 815, 560)
        scrollArea.setFrameShape(0)

        scrollAreaWidgetContents.show()
        scrollArea.show()

        picCount = 0
        for photo in photos:
            picX = int(picCount % _LINE_PIC_NUM)
            picY = int(picCount / _LINE_PIC_NUM)

            border = QtWidgets.QLabel()
            border.setGeometry(picX * _MINI_POS_SIZE + 7, picY * _MINI_POS_SIZE + 7,
                              _MINISIZE+4, _MINISIZE+4)
            border.setParent(scrollAreaWidgetContents)
            border.show()

            label = myPicLabel(photo)
            label.setGeometry(picX * _MINI_POS_SIZE + 9 + int((_MINISIZE-photo.getWidth())/2), picY * _MINI_POS_SIZE + 9,
                              _MINISIZE, _MINISIZE)
            label.setParent(scrollAreaWidgetContents)
            label.setPixmap(QPixmap.fromImage(photo.getPhoto()))

            if photo.iamTrue() == 1:
                border.setStyleSheet(rightStyle)
                rightNUM += 1
            elif photo.iamTrue() == 2:
                border.setStyleSheet(wrongStyle)
                wrongNUM += 1
            else:
                border.setStyleSheet(normalStyle)
            label.show()
            picCount += 1

        self.ui.rightNUM.setText(str(rightNUM))
        self.ui.wrongNUM.setText(str(wrongNUM))
        self.ui.bird.setText(self.photoDataKeys[index].split('/')[0].replace('_', ' '))

        if self.picSearchState:
            self.ui.mAP1.setText(str(round(self.mAP[0], 3)))
            self.ui.mAP2.setText(str(round(self.mAP[1], 3)))
            self.ui.mAP3.setText(str(round(self.mAP[2], 3)))
            self.ui.mAP4.setText(str(round(self.mAP[3], 3)))

    def _reset(self):
        pass

    def searchingState(self, state):
        if state:
            self.ui.bird.setText("Searching...")
        else:
            self.ui.bird.setText("Done !")

    def startTime(self):
        self.s_now = datetime.datetime.now()

    def endTime(self):
        spend = datetime.datetime.now() - self.s_now
        ms = spend.microseconds
        ms /= 1000.0
        ss = spend.seconds
        self.ui.spendtime.setText("%d.%.0f s" % (ss, ms))

    def gotoSearch(self, text):
        if text != "":
            self.startTime()
            self.searchThreadTXT.setKeyword(text)
            self.searchThreadTXT.start()
            self.searchingState(True)
        else:
            print("NOT NULL FOR KEYWORD")

    def showResult(self, res):
        self.endTime()
        self.searchingState(False)
        self.searchThreadTXT.quit()
        self._reset()
        if res != {}:
            self._showPic(res)
        else:
            self._showEmpty()

    def showResultOnModel(self, res):
        self.endTime()
        self.picSearchState = True
        self.searchingState(False)
        self.searchThreadTXT.quit()
        self._reset()
        if res != {}:
            self._showPic(res)
        else:
            self._showEmpty()

    def colectThreads(self, res):
        #self.mutex.lock()
        _result = {**res['pic'], **self.result['pic']}
        self.result['pic'] = _result
        self.threadsOK += 1
        #self.mutex.unlock()

        self.ui.spendtime.setText("%d / %d"%(self.threadsOK, self.threadsNUM))
        if self.threadsOK == self.threadsNUM:
            self.showResultOnModel(res)

    def gotoSearchOnModel(self, path):
        self.startTime()
        self.threadSingle = searchBirdByPic()
        self.threadSingle.setKeyword(path, net=self.network)
        self.threadSingle.SCsignal.connect(self.showResultOnModel)
        self.threadSingle.start()
        self.searchingState(True)
        self.setFather(path, True)
        return
        # multi thread
        self.threads = []
        self.threadsNUM = len(path)
        self.threadsOK = 0
        self.result = {'pic': {}, 'map': [1,1,1,1]}
        for p in path:
            self.threads.append(searchBirdByPic())
            self.threads[-1].setKeyword([p], net=self.network)
            self.threads[-1].SCsignal.connect(self.colectThreads)
            self.threads[-1].start()
        self.searchingState(True)
        self.setFather(path, True)

    def setFather(self, paths, PIC = False):
        if PIC:
            for p in paths:
                item = QtWidgets.QListWidgetItem(self.ui.listWidget)
                item.setIcon(QtGui.QIcon(p))
                item.setText(p.split('images')[1].split('.')[1].split('/')[1][:17] + "...")
                self.ui.listWidget.addItem(item)
        else:
            for p in paths:
                item = QtWidgets.QListWidgetItem(self.ui.listWidget)
                item.setText(p.split('.')[1].replace("_", " "))
                self.ui.listWidget.addItem(item)

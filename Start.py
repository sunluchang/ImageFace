# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
author  @   Sun Luchang
m_date  @   2019-05-01

UI for Digital-Image-Processing-HomeWork
'''

from config import _SYS_ROOT_PATH_
_LOGO_PATH = _SYS_ROOT_PATH_ + "img/logo.png"

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from ui_src.mainUI import Ui_MainWindow

from UIshow import showUI

from engine.search import realSearch, testNet

class mainUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(mainUI, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1000, 600)
        self.setWindowTitle(u'FourImage')
        self.ui.label.setPixmap(QPixmap(_LOGO_PATH))

        self.ui.goSearch.clicked.connect(self.gotoSearch)
        self.ui.addSearchFile.clicked.connect(self.selectFiles)

        self.ui.listWidget.close()
        self.ui.lineEdit.textChanged.connect(self.realSearch)

        self.realSearcher = realSearch()
        self.realSearcher.SCsignal.connect(self.showSearchRes)

        self.ui.listWidget.setMovement(QtWidgets.QListView.Static)
        self.ui.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.ui.listWidget.setSpacing(4)

        self.ui.listWidget.clicked.connect(self.getSelect)
        self.ui.slc.clicked.connect(self.slc)
        self.ui.czw.clicked.connect(self.czw)
        self.ui.ywt.clicked.connect(self.ywt)

        self.network = False
        self.connect = False
        self.rGroup = QtWidgets.QButtonGroup(self)
        self.rGroup.addButton(self.ui.local, 1)
        self.rGroup.addButton(self.ui.net, 2)
        self.rGroup.buttonClicked.connect(self.setNetWork)

        self.netThread = testNet()
        self.netThread.SCsignal.connect(self.testNetWork)
        self.netThread.start()

    def testNetWork(self, res):
        if res == 0:
            self.network = False
            self.connect = False
            self.ui.label_5.setStyleSheet("background-color:rgb(250, 66, 66); border-radius: 6px;")

        else:
            self.connect = True
            self.ui.label_5.setStyleSheet("background-color:rgb(0, 200, 0); border-radius: 6px;")


    def setNetWork(self):
        now = self.rGroup.checkedId()
        if self.connect:
            if now == 1:
                self.network = False
            else:
                self.network = True

    def getSelect(self):
        keyword = self.searchList[self.ui.listWidget.currentRow()]
        self.ui.lineEdit.clear()
        self.ui.listWidget.clear()
        self.ui.listWidget.close()
        self.showRes = showUI()
        self.showRes.gotoSearch(keyword)
        self.showRes.show()

    def gotoSearch(self):
        text = self.ui.lineEdit.text()
        if text.strip() != '':
            self.ui.lineEdit.clear()
            self.ui.listWidget.clear()
            self.ui.listWidget.close()
            self.showRes = showUI()
            self.showRes.gotoSearch(text)
            self.showRes.show()
        else:
            # warning empty
            reply = QtWidgets.QMessageBox.information(self, u'提示', u'请输入需要检索的鸟类别',  QtWidgets.QMessageBox.Yes)
            self.ui.lineEdit.setText('')

    def selectFiles(self):
        fileDialog = QtWidgets.QFileDialog.getOpenFileNames(self, "选择图片", "/Users/thatslc/Downloads/CUB_200_2011/CUB_200_2011/images", ("图片文件(*.png *.jpg)"))
        # fileDialog is a tuple ([files, ...], [format])
        if fileDialog[0]:
            # User select files
            self.selectFileList = fileDialog[0]
            if self.network:
                self.showRes2 = showUI(net=self.network)
            else:
                self.showRes2 = showUI()
            self.showRes2.show()
            self.showRes2.gotoSearchOnModel(self.selectFileList)

        else:
            print("User do not select files.")

    def realSearch(self):
        keyword = self.ui.lineEdit.text().lower()
        if keyword.strip() != '':
            self.realSearcher.setKeyword(keyword)
            self.realSearcher.start()
        else:
            self.ui.listWidget.close()

    def showSearchRes(self, res):
        self.ui.listWidget.clear()
        self.searchList = res
        for r in res:
            item = QtWidgets.QListWidgetItem()
            item.setText(r)
            self.ui.listWidget.addItem(item)
        if len(res) > 0:
            self.ui.listWidget.resize(QtCore.QSize(300, 26 * len(res) + 5))
            self.ui.listWidget.show()
        else:
            self.ui.listWidget.close()

    def slc(self):
        from UIslc import slcUI
        self.slcUI = slcUI()
        self.slcUI.show()

    def czw(self):
        from UIczw import czwUI
        self.czwUI = czwUI()
        self.czwUI.show()

    def ywt(self):
        from UIywt import ywtUI
        self.ywtUI = ywtUI()
        self.ywtUI.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    frm = mainUI()
    frm.show()
    sys.exit(app.exec_())
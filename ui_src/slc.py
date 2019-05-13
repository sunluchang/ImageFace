# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/thatslc/PycharmProjects/ImageFace/ui_files/slc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(602, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 10, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.aa = QtWidgets.QPushButton(self.centralwidget)
        self.aa.setGeometry(QtCore.QRect(480, 110, 113, 32))
        self.aa.setObjectName("aa")
        self.bb = QtWidgets.QPushButton(self.centralwidget)
        self.bb.setGeometry(QtCore.QRect(480, 140, 113, 32))
        self.bb.setObjectName("bb")
        self.cc = QtWidgets.QPushButton(self.centralwidget)
        self.cc.setGeometry(QtCore.QRect(480, 170, 113, 32))
        self.cc.setObjectName("cc")
        self.raw = QtWidgets.QLabel(self.centralwidget)
        self.raw.setGeometry(QtCore.QRect(20, 10, 200, 200))
        self.raw.setObjectName("raw")
        self.a = QtWidgets.QLabel(self.centralwidget)
        self.a.setGeometry(QtCore.QRect(250, 10, 200, 200))
        self.a.setObjectName("a")
        self.b = QtWidgets.QLabel(self.centralwidget)
        self.b.setGeometry(QtCore.QRect(20, 240, 200, 200))
        self.b.setObjectName("b")
        self.c = QtWidgets.QLabel(self.centralwidget)
        self.c.setGeometry(QtCore.QRect(250, 240, 200, 200))
        self.c.setObjectName("c")
        self.raw_2 = QtWidgets.QLabel(self.centralwidget)
        self.raw_2.setGeometry(QtCore.QRect(20, 210, 200, 21))
        self.raw_2.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_2.setObjectName("raw_2")
        self.raw_3 = QtWidgets.QLabel(self.centralwidget)
        self.raw_3.setGeometry(QtCore.QRect(250, 210, 200, 21))
        self.raw_3.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_3.setObjectName("raw_3")
        self.raw_4 = QtWidgets.QLabel(self.centralwidget)
        self.raw_4.setGeometry(QtCore.QRect(20, 440, 200, 21))
        self.raw_4.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_4.setObjectName("raw_4")
        self.raw_5 = QtWidgets.QLabel(self.centralwidget)
        self.raw_5.setGeometry(QtCore.QRect(250, 440, 200, 21))
        self.raw_5.setAlignment(QtCore.Qt.AlignCenter)
        self.raw_5.setObjectName("raw_5")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(490, 210, 91, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 230, 91, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SLC"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.aa.setText(_translate("MainWindow", "算术均值"))
        self.bb.setText(_translate("MainWindow", "几何均值"))
        self.cc.setText(_translate("MainWindow", "自适应"))
        self.raw.setText(_translate("MainWindow", "raw"))
        self.a.setText(_translate("MainWindow", "raw"))
        self.b.setText(_translate("MainWindow", "raw"))
        self.c.setText(_translate("MainWindow", "raw"))
        self.raw_2.setText(_translate("MainWindow", "原始"))
        self.raw_3.setText(_translate("MainWindow", "算术"))
        self.raw_4.setText(_translate("MainWindow", "几何"))
        self.raw_5.setText(_translate("MainWindow", "自适应"))
        self.label.setText(_translate("MainWindow", "0"))


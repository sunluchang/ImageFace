# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/thatslc/PycharmProjects/ImageFace/ui_files/mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 280, 561, 41))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("border-radius: 20px;\n"
"padding-left: 10px;\n"
"font-size:  15pt;\n"
"background-color: #f5f5f5;\n"
"color: #232323;\n"
"outline: \'none\';")
        self.lineEdit.setObjectName("lineEdit")
        self.goSearch = QtWidgets.QPushButton(self.centralwidget)
        self.goSearch.setGeometry(QtCore.QRect(680, 330, 100, 30))
        self.goSearch.setMinimumSize(QtCore.QSize(100, 30))
        self.goSearch.setMaximumSize(QtCore.QSize(100, 30))
        self.goSearch.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    border: 1px solid #cccccc;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: #dddddd;\n"
"}")
        self.goSearch.setObjectName("goSearch")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 110, 481, 91))
        self.label.setText("")
        self.label.setObjectName("label")
        self.addSearchFile = QtWidgets.QPushButton(self.centralwidget)
        self.addSearchFile.setGeometry(QtCore.QRect(570, 330, 100, 30))
        self.addSearchFile.setMinimumSize(QtCore.QSize(100, 30))
        self.addSearchFile.setMaximumSize(QtCore.QSize(100, 30))
        self.addSearchFile.setStyleSheet("QPushButton{\n"
"    border-radius: 15px;\n"
"    border: 1px solid #cccccc;\n"
"    background-color: #ffffff;\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: #dddddd;\n"
"}")
        self.addSearchFile.setObjectName("addSearchFile")
        self.ywt = QtWidgets.QPushButton(self.centralwidget)
        self.ywt.setGeometry(QtCore.QRect(370, 440, 70, 70))
        self.ywt.setStyleSheet("border-radius: 35px;\n"
"border: 1px solid #ababab;")
        self.ywt.setObjectName("ywt")
        self.czw = QtWidgets.QPushButton(self.centralwidget)
        self.czw.setGeometry(QtCore.QRect(470, 440, 70, 70))
        self.czw.setStyleSheet("border-radius: 35px;\n"
"border: 1px solid #ababab;")
        self.czw.setObjectName("czw")
        self.slc = QtWidgets.QPushButton(self.centralwidget)
        self.slc.setGeometry(QtCore.QRect(570, 440, 70, 70))
        self.slc.setStyleSheet("border-radius: 35px;\n"
"border: 1px solid #ababab;")
        self.slc.setObjectName("slc")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 510, 71, 31))
        self.label_2.setStyleSheet("color: #aaa;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 510, 71, 31))
        self.label_3.setStyleSheet("color: #aaa;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 510, 71, 31))
        self.label_4.setStyleSheet("color: #aaa;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(230, 320, 541, 71))
        self.listWidget.setStyleSheet("border-left: 2px solid #dedede;\n"
"border-right: 2px solid #dedede;\n"
"border-bottom: 2px solid #dedede;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;")
        self.listWidget.setObjectName("listWidget")
        self.local = QtWidgets.QRadioButton(self.centralwidget)
        self.local.setGeometry(QtCore.QRect(10, 570, 51, 20))
        self.local.setChecked(True)
        self.local.setObjectName("local")
        self.net = QtWidgets.QRadioButton(self.centralwidget)
        self.net.setGeometry(QtCore.QRect(60, 570, 51, 20))
        self.net.setObjectName("net")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(940, 577, 12, 12))
        self.label_5.setStyleSheet("width: 12px;\n"
"height: 12px;\n"
"border-radius: 6px;\n"
"background-color: rgb(250,66,66);\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(960, 575, 60, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FourImages"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "搜索类别"))
        self.goSearch.setText(_translate("MainWindow", "Search"))
        self.addSearchFile.setText(_translate("MainWindow", "Add"))
        self.ywt.setText(_translate("MainWindow", "形态学"))
        self.czw.setText(_translate("MainWindow", "FFT"))
        self.slc.setText(_translate("MainWindow", "滤波器"))
        self.label_2.setText(_translate("MainWindow", "袁文涛"))
        self.label_3.setText(_translate("MainWindow", "曹志崴"))
        self.label_4.setText(_translate("MainWindow", "孙路畅"))
        self.local.setText(_translate("MainWindow", "本地"))
        self.net.setText(_translate("MainWindow", "网络"))
        self.label_6.setText(_translate("MainWindow", "网络"))


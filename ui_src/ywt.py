# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/thatslc/PycharmProjects/ImageFace/ui_files/ywt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(702, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 30, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(520, 60, 113, 32))
        self.start.setObjectName("start")
        self.t1 = QtWidgets.QLabel(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(20, 10, 200, 200))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLabel(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(250, 10, 200, 200))
        self.t2.setObjectName("t2")
        self.t3 = QtWidgets.QLabel(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(20, 240, 200, 200))
        self.t3.setObjectName("t3")
        self.t4 = QtWidgets.QLabel(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(250, 240, 200, 200))
        self.t4.setObjectName("t4")
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
        self.raw = QtWidgets.QLabel(self.centralwidget)
        self.raw.setGeometry(QtCore.QRect(480, 240, 200, 200))
        self.raw.setObjectName("raw")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(540, 110, 100, 20))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(540, 140, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(540, 170, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.slider = QtWidgets.QSlider(self.centralwidget)
        self.slider.setGeometry(QtCore.QRect(530, 200, 91, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 220, 91, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YWT"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.t1.setText(_translate("MainWindow", "raw"))
        self.t2.setText(_translate("MainWindow", "raw"))
        self.t3.setText(_translate("MainWindow", "raw"))
        self.t4.setText(_translate("MainWindow", "raw"))
        self.raw_2.setText(_translate("MainWindow", "close"))
        self.raw_3.setText(_translate("MainWindow", "dilate"))
        self.raw_4.setText(_translate("MainWindow", "erode"))
        self.raw_5.setText(_translate("MainWindow", "open"))
        self.raw.setText(_translate("MainWindow", "raw"))
        self.radioButton.setText(_translate("MainWindow", "Rect"))
        self.radioButton_2.setText(_translate("MainWindow", "Cross"))
        self.radioButton_3.setText(_translate("MainWindow", "Ellipse"))
        self.label.setText(_translate("MainWindow", "1"))


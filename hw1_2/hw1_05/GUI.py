# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 201, 281))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.btn_loadImg = QtWidgets.QPushButton(self.groupBox)
        self.btn_loadImg.setGeometry(QtCore.QRect(30, 30, 141, 25))
        self.btn_loadImg.setObjectName("btn_loadImg")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 181, 211))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_showImg = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_showImg.setGeometry(QtCore.QRect(10, 20, 161, 25))
        self.btn_showImg.setObjectName("btn_showImg")
        self.btn_showMdlStruc = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_showMdlStruc.setGeometry(QtCore.QRect(10, 70, 161, 25))
        self.btn_showMdlStruc.setObjectName("btn_showMdlStruc")
        self.btn_showDataAug = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_showDataAug.setGeometry(QtCore.QRect(10, 120, 161, 25))
        self.btn_showDataAug.setObjectName("btn_showDataAug")
        self.btn_inference = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_inference.setGeometry(QtCore.QRect(10, 170, 161, 25))
        self.btn_inference.setObjectName("btn_inference")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(230, 40, 256, 241))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "5. Cifar10 Classifier using VGG16"))
        self.btn_loadImg.setText(_translate("MainWindow", "Load Image"))
        self.btn_showImg.setText(_translate("MainWindow", "1. Show Train Images"))
        self.btn_showMdlStruc.setText(_translate("MainWindow", "2. Show Model Structure"))
        self.btn_showDataAug.setText(_translate("MainWindow", "3. Show Data Augmentation"))
        self.btn_inference.setText(_translate("MainWindow", "5. Inference"))
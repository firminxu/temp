# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 190, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 110, 421, 57))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dLineEdit.sizePolicy().hasHeightForWidth())
        self.dLineEdit.setSizePolicy(sizePolicy)
        self.dLineEdit.setObjectName("dLineEdit")
        self.gridLayout.addWidget(self.dLineEdit, 0, 1, 1, 1)
        self.dLable = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dLable.sizePolicy().hasHeightForWidth())
        self.dLable.setSizePolicy(sizePolicy)
        self.dLable.setObjectName("dLable")
        self.gridLayout.addWidget(self.dLable, 0, 0, 1, 1)
        self.sLable = QtWidgets.QLabel(self.layoutWidget)
        self.sLable.setObjectName("sLable")
        self.gridLayout.addWidget(self.sLable, 1, 0, 1, 1)
        self.dOutLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dOutLabel.sizePolicy().hasHeightForWidth())
        self.dOutLabel.setSizePolicy(sizePolicy)
        self.dOutLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.dOutLabel.setLineWidth(1)
        self.dOutLabel.setObjectName("dOutLabel")
        self.gridLayout.addWidget(self.dOutLabel, 0, 2, 1, 1)
        self.sLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.sLineEdit.setObjectName("sLineEdit")
        self.gridLayout.addWidget(self.sLineEdit, 1, 1, 1, 1)
        self.sOutLabel = QtWidgets.QLabel(self.layoutWidget)
        self.sOutLabel.setObjectName("sOutLabel")
        self.gridLayout.addWidget(self.sOutLabel, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dLable.setBuddy(self.dLineEdit)
        self.sLable.setBuddy(self.sLineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.dLable.setText(_translate("MainWindow", "请输入一个偶数(&D)"))
        self.sLable.setText(_translate("MainWindow", "请输入一个奇数(&S)"))
        self.dOutLabel.setText(_translate("MainWindow", "请输入"))
        self.sOutLabel.setText(_translate("MainWindow", "请输入"))
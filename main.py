# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Oct 25 21:26:19 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1586, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1537, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1260, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(900, 862))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(900, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeView = QtWidgets.QTreeView(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QtCore.QSize(250, 0))
        self.treeView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeView.setAutoScrollMargin(0)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.frame_12 = QtWidgets.QFrame(self.frame_7)
        self.frame_12.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton = QtWidgets.QPushButton(self.frame_12)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_12)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMinimumSize(QtCore.QSize(250, 0))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_6.addWidget(self.treeWidget)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_5)
        self.frame_10.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_13 = QtWidgets.QFrame(self.frame_10)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.frame_13)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.treeWidget_2.headerItem().setText(0, "1")
        self.horizontalLayout_4.addWidget(self.treeWidget_2)
        self.verticalLayout_7.addWidget(self.frame_13)
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_10.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_10.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_10.addWidget(self.pushButton_5)
        self.verticalLayout_7.addWidget(self.frame_11)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(900, 300))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 361))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_14 = QtWidgets.QFrame(self.frame_6)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.frame_14)
        self.treeWidget_3.setObjectName("treeWidget_3")
        self.treeWidget_3.headerItem().setText(0, "1")
        self.verticalLayout_10.addWidget(self.treeWidget_3)
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setMinimumSize(QtCore.QSize(0, 10))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.horizontalLayout_8.addWidget(self.frame_14)
        self.verticalLayout.addWidget(self.frame_6)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(606, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(9, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add to file stack", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "remove file", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Template it !", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "add category", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "temp/OCR/tittle", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "remove", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "Scan files", None, -1))
        self.pushButton_8.setText(QtWidgets.QApplication.translate("MainWindow", "Validate results", None, -1))

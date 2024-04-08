# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiScrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(352, 426)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(352, 426))
        mainWindow.setMaximumSize(QtCore.QSize(352, 426))
        mainWindow.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 130, 101, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 210, 291, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setDragEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 290, 291, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_3.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setDragEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 251, 41))
        self.label.setStyleSheet("font: 100 11pt \"Waree\"; alignment: center;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 151, 21))
        self.label_2.setStyleSheet("font: 11pt \"Waree\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 91, 21))
        self.label_3.setStyleSheet("font: 11pt \"Waree\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 171, 21))
        self.label_4.setStyleSheet("font: 11pt \"Waree\";")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 370, 311, 25))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(24, 24, 24);\n"
"background-color: rgb(17, 16, 16);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 171, 21))
        self.label_5.setStyleSheet("font: 11pt \"Waree\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 340, 171, 21))
        self.label_7.setStyleSheet("font: 11pt \"Waree\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 370, 311, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setDragEnabled(True)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 171, 20))
        self.label_8.setStyleSheet("font: 11pt \"Waree\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 260, 121, 20))
        self.label_9.setStyleSheet("font: 11pt \"Waree\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(210, 180, 121, 20))
        self.label_10.setStyleSheet("font: 11pt \"Waree\";")
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 340, 101, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(17, 16, 16);\n"
"border-top-color: rgb(238, 238, 236);\n"
"color: rgb(238, 238, 236);\n"
"selection-background-color: rgb(24, 24, 24);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 130, 101, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit_5.setDragEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 130, 91, 25))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAccessibleDescription("")
        self.lineEdit_6.setStyleSheet("selection-background-color: rgb(24, 24, 24);")
        self.lineEdit_6.setDragEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(170, 100, 161, 20))
        self.label_12.setStyleSheet("font: 11pt \"Waree\";")
        self.label_12.setObjectName("label_12")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(320, 210, 16, 23))
        self.radioButton.setStyleSheet("selection-background-color: rgb(32, 32, 32);")
        self.radioButton.setText("")
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 290, 16, 23))
        self.radioButton_2.setStyleSheet("selection-background-color: rgb(32, 32, 32);")
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 340, 71, 25))
        self.pushButton_3.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"border-top-color: rgb(52, 52, 52);\n"
"color: rgb(238, 238, 236);\n"
"selection-background-color: rgb(24, 24, 24);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.qr_mask_label = QtWidgets.QLabel(self.centralwidget)
        self.qr_mask_label.setGeometry(QtCore.QRect(50, 90, 256, 256))
        self.qr_mask_label.setText("")
        self.qr_mask_label.setTextFormat(QtCore.Qt.AutoText)
        self.qr_mask_label.setPixmap(QtGui.QPixmap("data/qr_code_mask.png"))
        self.qr_mask_label.setScaledContents(False)
        self.qr_mask_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qr_mask_label.setWordWrap(False)
        self.qr_mask_label.setIndent(0)
        self.qr_mask_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.qr_mask_label.setObjectName("qr_mask_label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 370, 256, 25))
        self.pushButton_4.setStyleSheet("background-color: rgb(17, 16, 16);\n"
"border-top-color: rgb(238, 238, 236);\n"
"color: rgb(238, 238, 236);\n"
"selection-background-color: rgb(24, 24, 24);")
        self.pushButton_4.setObjectName("pushButton_4")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.lineEdit_2, self.radioButton)
        mainWindow.setTabOrder(self.radioButton, self.lineEdit_3)
        mainWindow.setTabOrder(self.lineEdit_3, self.radioButton_2)
        mainWindow.setTabOrder(self.radioButton_2, self.lineEdit_4)
        mainWindow.setTabOrder(self.lineEdit_4, self.pushButton)
        mainWindow.setTabOrder(self.pushButton, self.pushButton_3)
        mainWindow.setTabOrder(self.pushButton_3, self.pushButton_2)
        mainWindow.setTabOrder(self.pushButton_2, self.lineEdit_6)
        mainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_5)
        mainWindow.setTabOrder(self.lineEdit_5, self.lineEdit)
        mainWindow.setTabOrder(self.lineEdit, self.pushButton_4)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "uiScrypt [000000000000]"))
        self.lineEdit.setText(_translate("mainWindow", "1"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "p (1)"))
        self.label.setText(_translate("mainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#2e3436;\">ui</span><span style=\" font-size:20pt; font-weight:600;\">Scrypt</span></p></body></html>"))
        self.label_2.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Configuration</span></p></body></html>"))
        self.label_3.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Passphrase</span></p></body></html>"))
        self.label_4.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Salt (Unique word)</span></p></body></html>"))
        self.pushButton.setText(_translate("mainWindow", "Make Password!"))
        self.label_5.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Generate Password</span></p></body></html>"))
        self.label_7.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">In process...</span></p></body></html>"))
        self.label_8.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Resulted Password</span></p></body></html>"))
        self.label_9.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; color:#a40000;\">(!) Can\'t be empty</span></p></body></html>"))
        self.label_10.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; color:#a40000;\">(!) Can\'t be empty</span></p></body></html>"))
        self.pushButton_2.setToolTip(_translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("mainWindow", "Make new"))
        self.lineEdit_5.setText(_translate("mainWindow", "8"))
        self.lineEdit_5.setPlaceholderText(_translate("mainWindow", "r (8)"))
        self.lineEdit_6.setText(_translate("mainWindow", "1048576"))
        self.lineEdit_6.setPlaceholderText(_translate("mainWindow", "N (1048576)"))
        self.label_12.setText(_translate("mainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; color:#a40000;\">(!) Invalid Configuration</span></p></body></html>"))
        self.pushButton_3.setToolTip(_translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("mainWindow", "As QR"))
        self.pushButton_4.setToolTip(_translate("mainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_4.setText(_translate("mainWindow", "Close QR Code view and return back"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\RegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.setWindowModality(QtCore.Qt.NonModal)
        Register.resize(435, 426)
        Register.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Register.setMouseTracking(False)
        Register.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Register.setWindowIcon(icon)
        Register.setWindowOpacity(1.0)
        Register.setStyleSheet("background-color: rgb(255, 248, 222);")
        Register.setTabShape(QtWidgets.QTabWidget.Rounded)
        Register.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralWidget = QtWidgets.QWidget(Register)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 71))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(110, 180, 41, 21))
        self.label_2.setObjectName("label_2")
        self.RBTeacher = QtWidgets.QRadioButton(self.centralWidget)
        self.RBTeacher.setGeometry(QtCore.QRect(180, 180, 89, 16))
        self.RBTeacher.setObjectName("RBTeacher")
        self.RBStudent = QtWidgets.QRadioButton(self.centralWidget)
        self.RBStudent.setGeometry(QtCore.QRect(260, 180, 89, 16))
        self.RBStudent.setObjectName("RBStudent")
        self.LEAccount = QtWidgets.QLineEdit(self.centralWidget)
        self.LEAccount.setGeometry(QtCore.QRect(170, 50, 171, 20))
        self.LEAccount.setObjectName("LEAccount")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(90, 300, 61, 21))
        self.label_3.setObjectName("label_3")
        self.LETel = QtWidgets.QLineEdit(self.centralWidget)
        self.LETel.setGeometry(QtCore.QRect(170, 301, 171, 20))
        self.LETel.setObjectName("LETel")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(110, 240, 31, 21))
        self.label_4.setObjectName("label_4")
        self.LEPassword = QtWidgets.QLineEdit(self.centralWidget)
        self.LEPassword.setGeometry(QtCore.QRect(170, 240, 171, 20))
        self.LEPassword.setObjectName("LEPassword")
        self.PBConfirm = QtWidgets.QPushButton(self.centralWidget)
        self.PBConfirm.setGeometry(QtCore.QRect(130, 370, 75, 23))
        self.PBConfirm.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 173, 69), stop:0.375 rgba(255, 255, 155, 69), stop:0.423533 rgba(254, 255, 156, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 233, 144, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 236, 158, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.PBConfirm.setObjectName("PBConfirm")
        self.PBCancel = QtWidgets.QPushButton(self.centralWidget)
        self.PBCancel.setGeometry(QtCore.QRect(230, 370, 75, 23))
        self.PBCancel.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 173, 69), stop:0.375 rgba(255, 255, 155, 69), stop:0.423533 rgba(254, 255, 156, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 233, 144, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 236, 158, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.PBCancel.setObjectName("PBCancel")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 31, 16))
        self.label_5.setObjectName("label_5")
        self.LEName = QtWidgets.QLineEdit(self.centralWidget)
        self.LEName.setGeometry(QtCore.QRect(170, 120, 171, 20))
        self.LEName.setObjectName("LEName")
        Register.setCentralWidget(self.centralWidget)

        self.retranslateUi(Register)
        self.PBCancel.clicked.connect(Register.close)
        QtCore.QMetaObject.connectSlotsByName(Register)
        Register.setTabOrder(self.LEAccount, self.LEName)
        Register.setTabOrder(self.LEName, self.RBTeacher)
        Register.setTabOrder(self.RBTeacher, self.RBStudent)
        Register.setTabOrder(self.RBStudent, self.LEPassword)
        Register.setTabOrder(self.LEPassword, self.LETel)
        Register.setTabOrder(self.LETel, self.PBConfirm)
        Register.setTabOrder(self.PBConfirm, self.PBCancel)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "注册"))
        self.label.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:10pt;\">账户号</span></p><p><span style=\" font-size:10pt;\">（学号或工号）</span></p></body></html>"))
        self.label_2.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:10pt;\">类型</span></p></body></html>"))
        self.RBTeacher.setText(_translate("Register", "教师"))
        self.RBStudent.setText(_translate("Register", "学生"))
        self.label_3.setText(_translate("Register", "<html><head/><body><p>联系方式</p></body></html>"))
        self.label_4.setText(_translate("Register", "<html><head/><body><p>密码</p></body></html>"))
        self.PBConfirm.setText(_translate("Register", "确定"))
        self.PBCancel.setText(_translate("Register", "取消"))
        self.label_5.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:10pt;\">姓名</span></p></body></html>"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\hello.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 472)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.heading = QtWidgets.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(180, 30, 250, 31))
        self.heading.setMinimumSize(QtCore.QSize(250, 0))
        self.heading.setMaximumSize(QtCore.QSize(221, 31))
        self.heading.setObjectName("heading")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(510, 410, 75, 23))
        self.exit.setObjectName("exit")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(60, 90, 471, 291))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lePassword = QtWidgets.QLineEdit(self.tab)
        self.lePassword.setGeometry(QtCore.QRect(170, 110, 171, 31))
        self.lePassword.setObjectName("lePassword")
        self.labelAccount = QtWidgets.QLabel(self.tab)
        self.labelAccount.setGeometry(QtCore.QRect(90, 50, 51, 41))
        self.labelAccount.setObjectName("labelAccount")
        self.btnLogin = QtWidgets.QPushButton(self.tab)
        self.btnLogin.setGeometry(QtCore.QRect(280, 200, 111, 31))
        self.btnLogin.setStyleSheet("font: 87 9pt \"Bodoni MT Black\";")
        self.btnLogin.setObjectName("btnLogin")
        self.btnRegister = QtWidgets.QPushButton(self.tab)
        self.btnRegister.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.btnRegister.setStyleSheet("font: 87 9pt \"Bodoni MT Black\";")
        self.btnRegister.setObjectName("btnRegister")
        self.labelPassword = QtWidgets.QLabel(self.tab)
        self.labelPassword.setGeometry(QtCore.QRect(90, 110, 54, 31))
        self.labelPassword.setObjectName("labelPassword")
        self.leAccount = QtWidgets.QLineEdit(self.tab)
        self.leAccount.setGeometry(QtCore.QRect(170, 50, 171, 31))
        self.leAccount.setObjectName("leAccount")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(-9, -26, 481, 291))
        self.label_2.setStyleSheet("image: url(image/bg2.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.lePassword.raise_()
        self.labelAccount.raise_()
        self.btnLogin.raise_()
        self.btnRegister.raise_()
        self.labelPassword.raise_()
        self.leAccount.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.labelPassword_2 = QtWidgets.QLabel(self.tab_2)
        self.labelPassword_2.setGeometry(QtCore.QRect(90, 110, 54, 31))
        self.labelPassword_2.setObjectName("labelPassword_2")
        self.labelAccount_2 = QtWidgets.QLabel(self.tab_2)
        self.labelAccount_2.setGeometry(QtCore.QRect(60, 50, 101, 41))
        self.labelAccount_2.setObjectName("labelAccount_2")
        self.leAccount_2 = QtWidgets.QLineEdit(self.tab_2)
        self.leAccount_2.setGeometry(QtCore.QRect(170, 50, 171, 31))
        self.leAccount_2.setObjectName("leAccount_2")
        self.lePassword_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lePassword_2.setGeometry(QtCore.QRect(170, 110, 171, 31))
        self.lePassword_2.setObjectName("lePassword_2")
        self.btnLogin_2 = QtWidgets.QPushButton(self.tab_2)
        self.btnLogin_2.setGeometry(QtCore.QRect(190, 190, 111, 31))
        self.btnLogin_2.setStyleSheet("font: 87 9pt \"Bodoni MT Black\";")
        self.btnLogin_2.setObjectName("btnLogin_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(-9, -26, 481, 291))
        self.label_4.setStyleSheet("image: url(image/bg2.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.labelPassword_2.raise_()
        self.labelAccount_2.raise_()
        self.leAccount_2.raise_()
        self.lePassword_2.raise_()
        self.btnLogin_2.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-30, -20, 701, 511))
        self.label.setStyleSheet("image: url(image/bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.tabWidget.raise_()
        self.heading.raise_()
        self.exit.raise_()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.exit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.exit, self.leAccount_2)
        Dialog.setTabOrder(self.leAccount_2, self.lePassword_2)
        Dialog.setTabOrder(self.lePassword_2, self.btnLogin_2)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; text-decoration: underline;\">体育设施管理系统</span></p></body></html>"))
        self.exit.setText(_translate("Dialog", "退出"))
        self.labelAccount.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">账号:</span></p></body></html>"))
        self.btnLogin.setText(_translate("Dialog", "登陆"))
        self.btnRegister.setText(_translate("Dialog", "注册"))
        self.labelPassword.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">密码:</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "用户"))
        self.labelPassword_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">密码:</span></p></body></html>"))
        self.labelAccount_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">管理员号:</span></p></body></html>"))
        self.btnLogin_2.setText(_translate("Dialog", "登陆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "管理员"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

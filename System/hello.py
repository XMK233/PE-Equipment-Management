# -*- coding: utf-8 -*-
import sys
import pymysql   
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')
from Ui_hello import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QLabel, QLineEdit, QInputDialog)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from asyncio.locks import Event
from _overlapped import NULL
from windowTesting import MyWindow
from RegisterWindow import Register
from inquiryWindow import inquiryWindow
from managerInterface import managerInterface
class Hello(QDialog, Ui_Dialog):
    
    #database
    db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
    cursor = db.cursor()
    def __init__(self, parent=None):
        super(Hello, self).__init__(parent)
        self.setupUi(self)
        self.btnRegister.clicked.connect(self.on_btnRegister)  
        self.btnLogin.clicked.connect(self.on_btnLogin)
        self.btnLogin_2.clicked.connect(self.on_btnLoginManager)
        self.setWindowTitle( "欢迎！！")
        #
        self.register = None
        self.panel = None
        self.panelManager = None
        
    def on_btnRegister(self):
        self.db.commit()
        self.register = Register()
        self.register.show()
        return
    def on_btnLogin(self):
        self.db.commit()
        ac = self.leAccount.text()
        pw = self.lePassword.text()
        cmd = 'select passport from user where id = "' + ac + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        if r == None:
            QMessageBox.information(self, "Question", "用户不存在")
            return
        if r[0] == pw:
            self.panel = inquiryWindow(int(ac))
            self.panel.show()
            self.db.close()
            self.close()
            return
        elif r[0] != pw:
            QMessageBox.information(self, "Question", "密码错误")
    def on_btnLoginManager(self):
        self.db.commit()
        ac = self.leAccount_2.text()
        pw = self.lePassword_2.text()
        cmd = 'select passport from manager where id = "' + ac + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        if r == None:
            QMessageBox.information(self, "Question", "该管理员不存在")
            return
        if r[0] == pw:
            self.panelManager = managerInterface(ac)
            self.panelManager.show()
            self.db.close()
            self.close()
            return
        elif r[0] != pw:
            QMessageBox.information(self, "Question", "密码错误") 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tst = Hello()
    tst.show()
    sys.exit(app.exec_())
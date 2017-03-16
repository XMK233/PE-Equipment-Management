# -*- coding: utf-8 -*-
import sys
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')
import pymysql
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from Ui_hello import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QLabel, QLineEdit, QInputDialog)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_RegisterWindow import Ui_Register


class Register(QMainWindow, Ui_Register):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.PBConfirm.clicked.connect(self.on_BtnConfirm)
        
    def on_BtnConfirm(self):
        account = self.LEAccount.text()
        password = self.LEPassword.text()
        telNum = self.LETel.text()
        if self.RBStudent.isChecked():
            type = "student"
        elif self.RBTeacher.isChecked():
            type = "teacher"
        name = self.LEName.text()
        
        if telNum == "" or account == "" or password == "":
            return
        
        if account != None:
            print("niyade")
            db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")#so I can input chinese characters
            cursor = db.cursor()
            #cmd = "insert into account values ('%s','%s','%s','%s');" %(account, name, type, password)
            '''print(account)
            print(name)
            print(type)
            print(password)
            print(telNum)'''
            cmd = "insert into user values ('" + account + "','" + name + "','" + type + "','"+ password + "','" + telNum + "');"
            try:
                cursor.execute(cmd)
                db.commit()
                #db.close()
                text = QMessageBox.information(self, "Message", "账户创建成功")#, QMessageBox.Yes
                db.close()
                self.close()
                '''if text == QMessageBox.Yes:
                    self.close()'''
            except:
                print("niyade")
                #db.close()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    tst = Register()
    tst.show()
    sys.exit(app.exec_())
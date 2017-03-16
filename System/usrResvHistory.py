# -*- coding: utf-8 -*-
import sys
import cmd
import pymysql 
import datetime
from Qt import QDateTime
from unittest.test.test_program import InitialisableProgram
from cmd import Cmd
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')#import from other directory
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem, QMessageBox, QListWidgetItem
from PyQt5.QtWidgets import QApplication
from UsrResvHistory import UsrResvHistory
import random

class usrResvHistory(UsrResvHistory):
    def __init__(self, a, c, parent=None):
        #a is id number, c is the database
        super(UsrResvHistory, self).__init__(parent)
        self.setupUi(self)
        self.id =  str(a)
        self.db = c
        self.cursor = self.db.cursor()
        self.initializeResvList()
        self.LWResvRecord.itemClicked.connect(self.unreserve)
        self.PBRefresh.clicked.connect(self.initializeResvList)
        
    
    def initializeResvList(self):
        self.LWResvRecord.clear()
        self.db.commit()
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        cmd = 'select siteid, sitetype, time_sta, time_end from site_reserve where userid = "' + self.id + '";'
        self.cursor.execute(cmd)
        info = []
        for i in self.cursor:
            t = ""
            t = t + i[1] + " " + i[0] + " "  +"\n起讫时间为 " + i[2] + " " + i[3]
            #print(t)
            info.append(QListWidgetItem(t))#########
        for k in range (len(info)):
            self.LWResvRecord.insertItem(k + 1, info[k])            
        return
    def unreserve(self,obj):
        self.db.commit()
        reply = QMessageBox.question(self, "确认退订？", obj.text(), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            info = obj.text()
            k = info.split()
            #cmd = 'delete from site_reserve where siteid = "' + k[1] + '" and sitetype = "' + k[0] + '" and time_sta = "' + k[3] +' ' + k[4] + '" and time_end = "' + t[5] + ' ' + t[6] + '";'
            cmd = 'delete from site_reserve where siteid = "' + k[1] + '" '
            cmd1 = ' and sitetype = "' + k[0] + '"'
            cmd2 = ' and time_sta = "' + k[3] + ' ' + k[4] + '"'
            cmd3 = ' and time_end = "' + k[5] + ' ' + k[6] + '";'
            cmd += cmd1 + cmd2 + cmd3
            self.cursor.execute(cmd)
            self.db.commit()
            self.initializeResvList()
            #QMessageBox.information(self, "退订成功")
        else:
            return
        return
    
if __name__ == '__main__':
    db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
    #c = db.cursor()    
    app = QApplication(sys.argv) 
    dlg = usrResvHistory(14061075, db)
    dlg.show()
    sys.exit(app.exec_())  
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
from UsrFaciUseHistoryM import UsrFaciUseHistoryM
import random

class courtServiceStatus(UsrFaciUseHistoryM):
    def __init__(self, a, c, d, parent=None):
        #a is id number, c is the database
        super(UsrFaciUseHistoryM, self).__init__(parent)
        self.setupUi(self)
        self.id =  a
        self.db = c
        self.area = d
        self.cursor = self.db.cursor()
        #self.initializeTrigger()
        self.initializeResvList()
        #slots
        self.LWResvRecord.itemClicked.connect(self.unreserve)
        self.PBRefresh.clicked.connect(self.initializeResvList)
        
    def DataBaseExe(self, cmd):
        self.db.commit()
        self.cursor.execute(cmd)
        contain = []
        for i in self.cursor:
            contain.append(i)
        return contain
    '''def initializeTrigger(self):
        self.db.commit()
        cmd = 'create trigger site_serivce_status_change1 after delete on site_service for each row  update site set valid = "可用" where id = old.siteid and type = old.sitetype; '
        self.cursor.execute(cmd)
        self.db.commit()
        return '''
    def initializeResvList(self):
        self.LWResvRecord.clear()
        self.db.commit()
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        cmd = 'select * from site_service;'
        rec = self.DataBaseExe(cmd)
        info = []
        for i in rec:
            t = ""
            name = self.DataBaseExe('select distinct name from service where id = "' + i[4] + '";')
            t = t + i[1] + ' ' + i[0] + ' ' + i[2] + ' ' + i[3] + ' ' + name[0][0]
            #print(t)
            info.append(QListWidgetItem(t))#########
        for k in range (len(info)):
            self.LWResvRecord.insertItem(k + 1, info[k])            
        return
    def unreserve(self,obj):
        self.db.commit()
        reply = QMessageBox.question(self, "确定消除？", obj.text(), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            info = obj.text()
            k = info.split()
            #print(k[0])
            eid = self.DataBaseExe('select id from service where name = "' + k[4] + '";')
            #print(eid)
            #cmd = 'delete from site_reserve where siteid = "' + k[1] + '" and sitetype = "' + k[0] + '" and time_sta = "' + k[3] +' ' + k[4] + '" and time_end = "' + t[5] + ' ' + t[6] + '";'
            cmd = 'delete from site_service where siteid = "' + k[1] + '" '
            cmd1 = ' and sitetype = "' + k[0] + '"'
            cmd2 = ' and time_sta = "' + k[2] + '"'
            cmd3 = ' and time_end = "' + k[3] + '"'
            cmd4 = ' and serviceid = "' + eid[0][0] + '";'
            cmd += cmd1 + cmd2 + cmd3 + cmd4
            #print(cmd)
            self.cursor.execute(cmd)
            self.db.commit()
            self.initializeResvList()
            '''
            cmd = 'update site set valid = "可用" where id = "' + k[1] + '" and type = "' + k[0] + '";'
            #print(cmd)
            self.cursor.execute(cmd)
            self.db.commit()
            '''
        else:
            return
        return
if __name__ == '__main__':
    db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
    #c = db.cursor()    
    app = QApplication(sys.argv) 
    dlg = courtServiceStatus("14061075", db, "A1")
    dlg.show()
    sys.exit(app.exec_()) 
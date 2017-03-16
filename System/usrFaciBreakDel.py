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
from UsrFaciBreakDel import UsrFaciBreakDel

class usrFaciBreakDel(UsrFaciBreakDel):
    def __init__(self, a, c, d, parent=None):
        #a is id number, c is the database
        super(UsrFaciBreakDel, self).__init__(parent)
        self.setupUi(self)
        self.id =  a
        self.db = c
        self.area = d
        self.cursor = self.db.cursor()
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
    
    def initializeResvList(self):
        self.db.commit()
        self.LWResvRecord.clear()
        self.db.commit()
        cmd = 'select equipmentid, qty from equipment_break where userid = "' + self.id + '";'
        rec = self.DataBaseExe(cmd)
        info = []
        for i in rec:
            t = ""
            name = self.DataBaseExe('select distinct name, cost from equipment where id = "' + i[0] + '";')
            b = name[0][1]
            z = str(b)[0:len(b) - 2]
            t = t + name[0][0] + "  数量为:  " + i[1] + " 总价值： " + str(  int(i[1], 10) * int(z)  ) + "元"
            #print(t)
            info.append(QListWidgetItem(t))#########
        for k in range (len(info)):
            self.LWResvRecord.insertItem(k + 1, info[k])            
        return
    def unreserve(self,obj):
        self.db.commit()
        reply = QMessageBox.question(self, "确认归还？", obj.text(), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            info = obj.text()
            k = info.split()
            eid = self.DataBaseExe('select id from equipment where name = "' + k[0] + '";')
            cmd = 'delete from equipment_break where userid = "' + self.id + '" '
            cmd1 = ' and equipmentid = "' + eid[0][0] + '"'
            cmd2 = ' and qty = "' + k[2] + '";'
            cmd += cmd1 + cmd2
            self.cursor.execute(cmd)
            self.db.commit()
            self.initializeResvList()
            
            #recover the quantity
            cmd = 'select qty from area_equipment where equipid = "' + eid[0][0] + '" and areaid = "' + self.area + '";'
            #print(cmd)
            qty_origin = self.DataBaseExe(cmd)
            qty1 = int(k[2]) + int(qty_origin[0][0])
            cmd = 'update area_equipment set qty = "' + str(qty1) + '" where equipid = "' + eid[0][0] + '" and areaid = "' + self.area + '";'
            #print(cmd)
            self.DataBaseExe(cmd)
        else:
            return
        return
if __name__ == '__main__':
    db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
    #c = db.cursor()    
    app = QApplication(sys.argv) 
    dlg = usrFaciBreakDel("14061081", db, "A1")
    dlg.show()
    sys.exit(app.exec_()) 
# -*- coding: utf-8 -*-
import sys
import cmd
import pymysql 
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')#import from other directory
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QApplication
from UserReadMe import UserReadMe
from UsrFaciUse1 import UsrFaciUse
class usrFaciUse(UsrFaciUse):
    def __init__(self, a, parent=None):
        super(UsrFaciUse, self).__init__(parent)
        self.setupUi(self)
        self.db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
        self.cursor = self.db.cursor()
        self.id = str(a)
        self.initializeTable()
    def initializeTable(self):
        self.db.commit()
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        cmd = 'select * from equipment_use where userid = "' + self.id + '";'
        self.cursor.execute(cmd)
        item = []# all the records
        for i in self.cursor:
            item.append(i)
        if len(item) == 0:#if 
            return
        item_num = len(item)#the number of lines of records
        self.TWFacNumTim.setRowCount(item_num)
        c = 0;
        for i in item:
            ac = self.id#account
            eid = i[1]#facility id
            cmd = 'select name from equipment where id = "' + eid + '";'
            self.cursor.execute(cmd)
            t = self.cursor.fetchone()
            #facility name t[0] i[2], i[1]
            self.TWFacNumTim.setItem(c, 0, QTableWidgetItem(t[0]))
            self.TWFacNumTim.setItem(c, 1, QTableWidgetItem(i[3]))
            self.TWFacNumTim.setItem(c, 2, QTableWidgetItem(str(i[2])))
            c += 1
        return
    def closeEvent(self, event):    
        self.db.close()  

if __name__ == '__main__':
    app = QApplication(sys.argv) 
    dlg = usrFaciUse(14061075)
    dlg.show()
    sys.exit(app.exec_())           
        
        
        
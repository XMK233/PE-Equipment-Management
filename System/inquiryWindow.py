# -*- coding: utf-8 -*-
import sys
import cmd
import pymysql 
import datetime
from Qt import QDateTime
sys.path.append('G:\\eclipse mares programs\\Database Tests\\PE Resources Management\\UIs')#import from other directory
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtWidgets import QApplication
from UserReadMe import UserReadMe
from usrFaciUse import usrFaciUse
from faciBreak import faciBreak
from InquiryWindowSdudent import TabWidget
from UserReadMe1 import UserReadMe1
from usrResvHistory import usrResvHistory 
import random
def timeOverlap(oriB, oriE, proB, proE):
    if proB > oriB and proE > oriB:
        return False
    elif proB < oriE and proE < oriE:
        return False
    else:
        return True

class inquiryWindow(TabWidget):
    def __init__(self, a, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setupUi(self)
        self.db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
        self.cursor = self.db.cursor()
        self.id = str(a); # the account number
        self.rm = None #facility read me window
        self.ufu = None #user facility use window
        self.fb = None #user facility break record window
        self.rm1 = None #court read me window
        self.rh = None #reserve history and unreserve
        self.initializeWhole()
        #tab1
        self.initializeCBCampus()
        #tab2
        self.initializeSite()
        self.initializeCBCampus_2()
        self.initializeCBCourtNum()
        self.TWEqpmNumChange_Scan()
        self.initializeTWCourtUseRecord()
        #push button
        self.PBInquire.clicked.connect(self.on_btnPBInquire)
        self.PBReadme.clicked.connect(self.on_btnPBReadme)
        self.PBRecord.clicked.connect(self.on_btnPBRecord)
        self.PBDmgRec.clicked.connect(self.on_btnPBDmgRec)
        self.PBConfirmReservation.clicked.connect(self.reservation)
        self.PBConfirmReservation.clicked.connect(self.initializeTWCourtUseRecord)
        self.PBReadme_2.clicked.connect(self.on_btnPBReadme_2)
        self.PBRecord_2.clicked.connect(self.on_btnPBPBRecord_2)
        #slots
        self.CBCampus.currentIndexChanged.connect(self.TWEqpmNumChange_Scan)
        self.PBRefresh.clicked.connect(self.TWEqpmNumChange_Scan)
        #self.PBRefresh.clicked.connect(self.initializeTWCourtUseRecord)
        self.PBRefresh_2.clicked.connect(self.initializeTWCourtUseRecord)
        
        #self.CBCourt.currentIndexChanged.connect(self.initializeCBCampus_2)
        self.CBCourt.currentIndexChanged.connect(self.initializeCBCourtNum)
        self.CBCampus_2.currentIndexChanged.connect(self.initializeCBCourtNum)
        self.CBCourt.currentIndexChanged.connect(self.initializeTWCourtUseRecord)
        self.CBCampus_2.currentIndexChanged.connect(self.initializeTWCourtUseRecord)
        self.CBCourtNum.currentIndexChanged.connect(self.initializeTWCourtUseRecord)
        #self.CBCampus_2.currentIndexChanged.connect(self.initializeCBCourtNum)
        
    def initializeWhole(self):
        self.db.commit()
        cmd = 'select name, type from user where id = "' + self.id + '";'
        self.cursor.execute(cmd)
        t = self.cursor.fetchone()
        if t[1] == "student":
            self.setWindowTitle( "欢迎你， " + t[0] + " 同学")
        else:
            self.setWindowTitle( "欢迎你， " + t[0] + " 老师")
        return
    def initializeCBCampus(self):
        self.db.commit()
        cmd = 'select distinct areaid from area_equipment;'
        self.cursor.execute(cmd)
        for r in self.cursor:
            cursor1 = self.db.cursor()
            cmd1 = 'select distinct name_ from area where areaid = "' + r[0] + '";'
            cursor1.execute(cmd1)
            cpsName = cursor1.fetchone()
            self.CBCampus.addItem(cpsName[0])
    def initializeSite(self):
        self.db.commit()
        cmd = 'select distinct type from site;'
        self.cursor.execute(cmd)
        for r in self.cursor:
            self.CBCourt.addItem(r[0])
        return
    def initializeCBCampus_2(self):
        self.db.commit()
        '''self.CBCampus_2.addItem("沙河")'''
        self.CBCampus_2.clear()
        #name = self.CBCourt.currentText()
        cmd = 'select distinct name_ from area'
        self.cursor.execute(cmd)
        for r in self.cursor:
            self.CBCampus_2.addItem(r[0])
        return
    def initializeCBCourtNum(self):#可能有问题
        self.CBCourtNum.clear()
        self.db.commit()
        type = self.CBCourt.currentText()
        name = self.CBCampus_2.currentText()
        #print(type)###########3
        #print(name)############3
        cmd =  'select distinct areaid from area where name_ = "' + name + '";'
        self.cursor.execute(cmd)
        t = self.cursor.fetchone()
        sitearea = t[0]
        #print(sitearea)#######
        cmd = 'select id from site where type = "' + type + '" and sitearea = "' + sitearea + '";'
        #print(cmd)###########
        self.cursor.execute(cmd)
        bb = []
        for r in self.cursor:
            bb.append(r[0])
        for b in bb:
            #print(b)
            self.CBCourtNum.addItem(b)
        return
    def initializeTWCourtUseRecord(self):
        self.TWCourtUseRecord.clear()
        self.db.commit()
        self.TWCourtUseRecord.setHorizontalHeaderLabels(['开始时间','结束时间'])#clear
        cmd = 'select time_sta, time_end from site_reserve where siteid = "' + self.CBCourtNum.currentText() + '" and sitetype = "' + self.CBCourt.currentText() + '";'
        
        self.cursor.execute(cmd)
        p = 0
        for r in self.cursor:
            self.TWCourtUseRecord.setItem(p, 0, QTableWidgetItem(r[0]))#add table item
            self.TWCourtUseRecord.setItem(p, 1, QTableWidgetItem(r[1]))
            p += 1
        return
    
    def on_btnPBReadme(self):
        self.db.commit()
        self.rm = UserReadMe()
        self.rm.show()
    def on_btnPBRecord(self):
        self.db.commit()
        self.ufu = usrFaciUse(int(self.id))
        self.ufu.show()
    def on_btnPBDmgRec(self):
        self.db.commit()
        self.fb = faciBreak(int(self.id))
        self.fb.show()
    def on_btnPBReadme_2(self):
        self.db.commit()
        self.rm1 = UserReadMe1()
        self.rm1.show()
    def on_btnPBPBRecord_2(self):
        self.db.commit()
        self.rh = usrResvHistory(int(self.id), self.db)
        self.rh.show() 
    def on_btnPBInquire(self):
        self.db.commit()
        ctlg = self.LECatagory.text()
        if ctlg == "":
            return
        cmd = 'select distinct id from equipment where name = "' + ctlg + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        equipid = r[0]
        #get equip id 
        cpsName = self.CBCampus.currentText()
        cmd = 'select distinct areaid from area where name_ = "' + cpsName + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        areaid = r[0]
        #get area id
        cmd = 'select distinct qty from area_equipment where equipid = "' + equipid + '" and ' + 'areaid = "' + areaid + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        if r == None:
            self.LNeqpmNum.display(0)
        elif r != None:
            num = r[0]
            self.LNeqpmNum.display(num)
        #get the number
        return     
    def TWEqpmNumChange_Scan(self):        
        self.db.commit()
        cpsName = self.CBCampus.currentText()
        cmd = 'select distinct areaid from area where name_ = "' + cpsName + '";'
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        areaid = r[0]
        #get the area id
        cmd =  'select distinct equipid, qty from area_equipment where areaid = "' + areaid + '";'
        self.cursor.execute(cmd)
        tab = []
        for i in self.cursor:
            tab.append(i)
        #get the number of apparatus
        p = 0
        self.TWeqpmNum.clear()
        self.TWeqpmNum.setHorizontalHeaderLabels(['种类','数量'])
        #clear the table before the update       
        for k in tab:
            equipid = k[0]
            cmd = 'select distinct name from equipment where id = "' + equipid + '";'
            self.cursor.execute(cmd)
            t = self.cursor.fetchone()
            self.TWeqpmNum.setItem(p, 0, QTableWidgetItem(t[0]))#add table item
            self.TWeqpmNum.setItem(p, 1, QTableWidgetItem(k[1]))
            p += 1
        #set the tables
        return 
    def reservation(self):
        self.db.commit()
        startTime = self.DTEStartTime.date()
        '''startMonth = startTime.month()
        startDay = startTime.day()
        startHour = self.TEStartHour.time().hour()'''
        
        endTime = self.DTEStopTime.date()
        '''endMonth = endTime.month()
        endDay = endTime.day()
        endHour = self.TEEndHour.time().hour()'''
        
        start = QDateTime(startTime, self.TEStartHour.time())#pyqt time
        end = QDateTime(endTime, self.TEEndHour.time())
        
        start1 = start.toPyDateTime()#python time
        #print(str(start1))
        end1 = end.toPyDateTime()#comparable
        
        spanDay = (end1 - start1).days#span time
        spanHour = (end1 - start1).seconds / 3600
        if (int(spanDay)) < 0:
            QMessageBox.warning(self, "警告", "日期不合法")
            return
        #print(random.randint(1001, 9999))#####
        num = self.CBCourtNum.currentText()
        type = self.CBCourt.currentText()
        cmd = 'select distinct time_sta,time_end from site_reserve where siteid = "' + num + '" and sitetype = "' + type + '"; '
        #print(cmd)
        self.cursor.execute(cmd)
        for r in self.cursor:
            t1 = r[0] 
            t2 = r[1] 
            #print(t1, t2)
            #print(str(start1), str(end1))
            if timeOverlap(t1, t2, str(start1), str(end1)):
                QMessageBox.warning(self, "抱歉", "该时段本场地已被预定")
                return
            
        k = random.randint(1001, 9999)
        
        #on the black lists?
        cmd = 'select * from equipment_break where userid = "' + self.id + '";'
        self.cursor.execute(cmd)
        if self.cursor.fetchone() != None:
            QMessageBox.warning(self, "警告", "有损坏器材未补，预定失败")
            return
        else:
            #validity
            cmd = 'select valid from site where id = "' + num + '" and type = "'+ type + '";'
            self.cursor.execute(cmd)
            t = self.cursor.fetchone()
            if t[0] != "可用":
                QMessageBox.warning(self, "警告", "该场地暂时不可用")
                return
            
            cmd = "insert into site_reserve values ('" + num + "','" + type + "','" + self.id + "','"+ str(start1) + "','" + str(end1) + "','" + str(k) + "');"
            #print(cmd)
            self.cursor.execute(cmd)
            self.db.commit()
            QMessageBox.information(self, "信息", "预定成功")
            return
    def closeEvent(self, event): 
        self.db.commit()
        reply = QMessageBox.question(self, '信息', "确定退出?    ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:  
            self.db.close()           
            event.accept()      
        else:             
            event.ignore()
             
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    dlg = inquiryWindow(14061075)
    dlg.show()
    sys.exit(app.exec_())
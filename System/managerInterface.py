# -*- coding: utf-8 -*-
import sys
import cmd
import pymysql 
import datetime
from Qt import QDateTime
from eric6.E5Gui.E5MessageBox import Close
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
from ManagerInterface import ManagerInterface
from usrFaciUseHistoryM import usrFaciUseHistoryM
from usrFaciBreakDel import usrFaciBreakDel
from CourtServiceStatus import courtServiceStatus
import time

class managerInterface(ManagerInterface):
    
    def __init__(self, a, parent=None):
        super(ManagerInterface, self).__init__(parent)
        self.setupUi(self)
        self.id = a#account
        self.db = pymysql.connect(host = "localhost", user = "root", passwd = "xmk19960915", db = "database", charset = "utf8")
        self.cursor = self.db.cursor()#database initialization
        self.campus = "";
        #initialization
        self.initializeTitle()
        
        self.initializeArea()
        self.initializeTWEquipOverviewAndCB()
        self.initializeTWUseOverview()
        self.initializeCBSupplier()
        self.initializeCBEquipName()
        self.initializeEquipBreak()
        
        self.initializeTWCourtOverView()
        self.initializeTWResvOverview()
        self.initializeTWServOverview()
        self.initializeCBCourtType()
        self.initializeCBCourtNum_2()
        self.initializeCBCourt()
        self.initializeCBCourtNum()
        self.initializaCBServer()
        #attributes
        self.ur = None #facility use record
        self.br = None #break record
        self.e = None# service end
        #slot 
        self.CBEquipment.currentIndexChanged.connect(self.changeLCD)
        self.PBLendEquip.clicked.connect(self.btn_PBLendEquip)
        self.PBLendEquip.clicked.connect(self.changeLCD)
        self.PBLendEquip.clicked.connect(self.initializeTWEquipOverviewAndCB)
        self.PBSeeRecord.clicked.connect(self.btn_PBSeeRecord)
        self.PBConfirmAddSupplier.clicked.connect(self.btn_PBConfirmAddSupplier)
        self.PBConfirmAddSupplier.clicked.connect(self.initializeCBSupplier)
        self.PBConfirmAdd.clicked.connect(self.btn_PBConfirmAdd)
        self.PBConfirmBroke.clicked.connect(self.btn_PBConfirmBroke)
        #self.PBConfirmBroke.clicked.connect()
        self.PBDelBorkRec.clicked.connect(self.btn_PBDelBorkRec)
        self.PBRefresh.clicked.connect(self.btn_PBRefresh)
        #self.PBRefresh.clicked.connect(self.initializeTWResvOverview)
        
        self.CBCourt.currentIndexChanged.connect(self.initializeCBCourtNum)
        self.PBRefresh_2.clicked.connect(self.initializeTWCourtOverView)
        self.PBRefresh_2.clicked.connect(self.initializeTWServOverview)
        self.PBRefresh_2.clicked.connect(self.initializeEquipBreak)
        self.PBConfirm.clicked.connect(self.btn_PBConfirm)
        self.PBEnd.clicked.connect(self.btn_PBEnd)
        self.PBConfirm_2.clicked.connect(self.btn_PBConfirm_2)
        self.CBCourtType.currentIndexChanged.connect(self.initializeCBCourtNum_2)
        self.PBValid.clicked.connect(self.btn_PBValid)
        self.PBInvalid.clicked.connect(self.btn_PBInvalid)
        self.PBConfirm_4.clicked.connect(self.btn_PBConfirm_4)
        return 
    def DataBaseExe(self, cmd):
        self.db.commit()
        self.cursor.execute(cmd)
        contain = []
        for i in self.cursor:
            contain.append(i)
        return contain
    def initializeTitle(self):
        self.db.commit()
        cmd = 'select name, area from manager where id = "' + self.id + '";'
        self.cursor.execute(cmd)
        t = self.cursor.fetchone()
        #print(t)
        cmd = 'select name_ from area where areaid = "' + t[1] + '";'
        b = self.DataBaseExe(cmd)
        self.setWindowTitle( "管理员： " + t[0] + "-_- 管理校区：" + b[0][0])
        
        #cmd = 'create trigger site_serivce_status_change 'asdfa
        return
    '''def initializeTrigger(self):
        self.db.commit()
        cmd = 'create trigger site_serivce_status_change1 after insert on site_service for each row  update site set valid = "不可用" where id = new.siteid and type = new.sitetype; '
        self.cursor.execute(cmd)
        self.db.commit()
        cmd = 'create trigger site_serivce_status_change2 after insert on site_service for each row  update site set valid = "不可用" where id = new.siteid and type = new.sitetype; '
        return'''
    def initializeArea(self):
        self.db.commit()
        cmd = 'select area from manager where id = "' + self.id + '";'
        #print(cmd)
        self.cursor.execute(cmd)
        t = self.cursor.fetchone()
        self.campus = t[0]
        #print(self.campus)
        return
    def initializeTWEquipOverviewAndCB(self):
        self.TWEquipOverview.clear()
        self.db.commit()
        self.TWEquipOverview.setHorizontalHeaderLabels(['器材名','可用数量'])#clear
        self.CBEquipment.clear()
        
        cmd = 'select equipid, qty from area_equipment where areaid = "' + self.campus + '";'
        self.cursor.execute(cmd)
        tab = []
        for i in self.cursor:
            tab.append(i)
        #get the number of apparatus
        p = 0
        n = len(tab)
        self.TWEquipOverview.setRowCount(n)
        for k in tab:
            equipid = k[0]
            cmd = 'select distinct name from equipment where id = "' + equipid + '";'
            self.cursor.execute(cmd)
            t = self.cursor.fetchone()
            self.TWEquipOverview.setItem(p, 0, QTableWidgetItem(t[0]))#add table item
            self.TWEquipOverview.setItem(p, 1, QTableWidgetItem(k[1]))
            self.CBEquipment.addItem(t[0])
            p += 1
        self.changeLCD()
        return
    
    def changeLCD(self):
        self.db.commit()
        
        ctlg = self.CBEquipment.currentText()
        if ctlg == "":
            return
        cmd = 'select distinct id from equipment where name = "' + ctlg + '";'
        #print(cmd)
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        equipid = r[0]
        
        
        cmd = 'select distinct qty from area_equipment where equipid = "' + equipid + '";'
        #print(cmd)
        self.cursor.execute(cmd)
        r = self.cursor.fetchone()
        num = r[0]
        
        self.LCDRemain.display(num)
        return 
    
    def initializeTWUseOverview(self):
        self.TWUseOverview.clear()
        self.db.commit()
        self.TWUseOverview.setHorizontalHeaderLabels(['种类','数量','账号', '姓名','联系方式'])#clear
        #self.TWUseOverview.setHorizontalHeaderLabels(['种类','数量', '姓名','联系方式'])#clear
        
        cmd = 'select * from equipment_use;'
        use_status = self.DataBaseExe(cmd)
        n = len(use_status)
        self.TWUseOverview.setRowCount(n)
        for i in range(n):
            userid = use_status[i][0]
            equipmentid = use_status[i][1]
            qty = use_status[i][3]
            
            name_tel = self.DataBaseExe('select distinct name, tel from user where id = "' + userid + '";')#name and communicate
            equipName = self.DataBaseExe('select distinct name from equipment where id = "' + equipmentid + '";')#only one
            #print(equipName[0][0])
            
            self.TWUseOverview.setItem(i, 0, QTableWidgetItem(equipName[0][0]))#add table item
            self.TWUseOverview.setItem(i, 1, QTableWidgetItem(qty))
            self.TWUseOverview.setItem(i, 2, QTableWidgetItem(userid))
            self.TWUseOverview.setItem(i, 3, QTableWidgetItem(name_tel[0][0]))#add table item
            self.TWUseOverview.setItem(i, 4, QTableWidgetItem(name_tel[0][1]))
            
        return            
    
    def initializeEquipBreak(self):
        self.TWBreakOverview.clear()
        self.db.commit()
        self.TWBreakOverview.setHorizontalHeaderLabels(['种类','数量','账号', '姓名','联系方式'])#clear
        cmd = 'select * from equipment_break;'
        use_status = self.DataBaseExe(cmd)
        n = len(use_status)
        self.TWBreakOverview.setRowCount(n)
        for i in range(n):
            userid = use_status[i][0]
            equipmentid = use_status[i][1]
            qty = use_status[i][2]
            
            name_tel = self.DataBaseExe('select distinct name, tel from user where id = "' + userid + '";')#name and communicate
            equipName = self.DataBaseExe('select distinct name from equipment where id = "' + equipmentid + '";')#only one
            #print(equipName[0][0])
            
            self.TWBreakOverview.setItem(i, 0, QTableWidgetItem(equipName[0][0]))#add table item
            self.TWBreakOverview.setItem(i, 1, QTableWidgetItem(qty))
            self.TWBreakOverview.setItem(i, 2, QTableWidgetItem(userid))
            self.TWBreakOverview.setItem(i, 3, QTableWidgetItem(name_tel[0][0]))#add table item
            self.TWBreakOverview.setItem(i, 4, QTableWidgetItem(name_tel[0][1]))
        return  
    
    def initializeCBSupplier(self):
        self.db.commit()
        self.CBSupplier.clear()
        names = self.DataBaseExe('select name from supplier')
        for i in names:
            self.CBSupplier.addItem(i[0])
    
    def initializeCBEquipName(self):
        self.db.commit()
        self.CBEquipName.clear()
        names = self.DataBaseExe('select name from equipment;')
        for i in names:
            self.CBEquipName.addItem(i[0])
    
    def closeEvent(self, event): 
        reply = QMessageBox.question(self, '信息', "确定退出?    ", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:  
            self.db.close()           
            event.accept()      
        else:             
            event.ignore()
    
    def btn_PBLendEquip(self):
        self.db.commit()
        userid = self.LEUser.text()
        qty = self.SBQuantity.value()
        equipName = self.CBEquipment.currentText()
        #print(userid)
        if userid == "" :
            return
        if qty == 0:
            return 
        if equipName == "":
            return
        
        #on the blacklist?
        cmd = 'select * from equipment_break where userid = "' + userid + '";'
        self.cursor.execute(cmd)
        if self.cursor.fetchone() != None:
            QMessageBox.warning(self, "警告", "有损坏器材未补，预定失败")
            return
        
        temp = self.DataBaseExe('select id from equipment where name = "' + equipName + '";')
        equipid = temp[0][0]
        
        cmd = 'select qty from area_equipment where equipid = "' + equipid + '" and areaid = "' + self.campus + '";'
        nums = self.DataBaseExe(cmd)
        num = int(nums[0][0])
        remain = num - qty
        if remain < 0:
            QMessageBox.warning(self, "警告", "剩余器材数量不足")
            return 
        t = time.strftime('%Y-%m-%d',time.localtime(time.time()))# GET current time
        cmd = 'insert into equipment_use values ("' + userid + '", "' + equipid + '", "' + t + '", "' + str(qty) + '");'
        #print (cmd)
        #self.DataBaseExe(cmd)
        try:
            self.cursor.execute(cmd)
            self.db.commit()
            self.initializeTWUseOverview()
            
            cmd = 'update area_equipment set qty = "' + str(remain) + '" where equipid = "' + equipid + '" and areaid = "' + self.campus + '";'
            #print(cmd)
            self.cursor.execute(cmd)
            self.db.commit()
            self.initializeTWEquipOverviewAndCB()
            QMessageBox.information(self, '信息', "借出成功") 
        except:
            return
        return
    def btn_PBSeeRecord(self):
        self.db.commit()
        userid = self.LEUser_2.text()
        
        if userid == "":
            return
        
        self.ur = usrFaciUseHistoryM(userid, self.db, self.campus)
        self.ur.show()
        
    def btn_PBRefresh(self):
        self.db.commit()
        self.initializeTWUseOverview()           
        self.initializeCBEquipName()
        self.initializeTWEquipOverviewAndCB()
        self.initializeEquipBreak()
        return
    
    def btn_PBConfirmAdd(self):
        self.db.commit()
        #get name
        self.db.commit()
        name = self.LEEquipName.text()
        if name == "":
            return 
        #get id
        ids = self.DataBaseExe('select id from equipment;')
        num = []
        b = 0
        for i in ids:
            k = i[0].split("E")
            if int(k[1]) > b:
                b = int(k[1])
        b = b + 1
        newId = "E" + str(b)
        #get supplier
        supplierName = self.CBSupplier.currentText()
        t = self.DataBaseExe('select id from supplier where name = "' + supplierName + '";')
        print(t)
        supplier = t[0][0]
        #get price
        
        if self.DSBPrice.value() == 0:
            return
        
        cost = str(self.DSBPrice.value())
        
        if self.SBQuantity_2.value() == 0:
            return
        
        qty = str(self.SBQuantity_2.value())
        #
        '''cmd = 'insert into equipment values("' + newId + '", "' + name + '", "' + supplier + '", "' + cost + '");'
        self.cursor.execute(cmd)
        self.db.commit()
        
        cmd = 'insert into area_equipment values("' + newId +'", "' + self.campus + '", "' + qty + '");'
        self.cursor.execute(cmd)
        self.db.commit()'''
        #sql function
        cmd = "call addEquipment('" + newId + "', '" + name + "', '" + supplier + "', '"+ cost + "', '" + self.campus + "', '" + qty + "');"
        print(cmd)
        self.cursor.execute(cmd)
        self.db.commit()
        #sql function
        self.initializeTWEquipOverviewAndCB() 
        QMessageBox.information(self, '信息', "添加成功")
        return
    def btn_PBConfirmAddSupplier(self):
        self.db.commit()
        name = self.LESupplierName.text()
        tel = self.LECommunicate_2.text()
        
        if name == "" or tel == "":
            return
        
        ids = self.DataBaseExe('select id from supplier;')
        num = []
        b = 0
        for i in ids:
            k = i[0].split("SU")
            if int(k[1]) > b:
                b = int(k[1])
        b = b + 1
        newId = "SU" + str(b)
        #cmd = 'insert into supplier values ("' + newId + '", "' + name + '", "' + tel + '");'
        #sql function
        cmd = "call addSupplier('" + newId + "', '" + name + "', '" + tel + "');"
        #sql function
        self.cursor.execute(cmd)
        self.db.commit()
        QMessageBox.information(self, '信息', "添加成功") 
        return
    
    def btn_PBConfirmBroke(self):
        self.db.commit()
        userid = self.LERespPerson.text()
        eqName = self.CBEquipName.currentText()
        t = self.DataBaseExe('select id from equipment where name = "' + eqName + '";')
        equipmentid = t[0][0]
        n = self.SBQuantity_3.value()
        
        if userid == "" or n == 0:
            return
        
        
        #
        cmd = 'select qty from area_equipment where equipid = "' + equipmentid + '" and areaid = "' + self.campus + '";'
        #print(cmd)
        nums = self.DataBaseExe(cmd)
        num = int(nums[0][0])
        remain = num - n
        
        
        qty = str(n)
        #sql function
        cmd = "call `database`.addBrakeRecord('" + userid + "', '" + qty + "', '" + str(remain)+ "', '" + equipmentid + "', '" + self.campus + "');"
        self.cursor.execute(cmd)
        self.db.commit()
        #sql functoin
        '''cmd = 'insert into equipment_break values ("' + userid + '", "' + equipmentid + '", "' + qty + '");'
        #print(cmd)
        self.cursor.execute(cmd)
        self.db.commit()
        cmd = 'update area_equipment set qty = "' + str(remain) + '" where equipid = "' + equipmentid + '" and areaid = "' + self.campus + '";'
        #print(cmd)
        self.cursor.execute(cmd)
        self.db.commit()'''
        self.initializeTWEquipOverviewAndCB()
        QMessageBox.information(self, '信息', "信息已添加") 
        self.initializeEquipBreak()
        return
    
    def btn_PBDelBorkRec(self):
        userid = self.LERespPerson.text()
        self.br = usrFaciBreakDel(userid, self.db, self.campus)
        self.br.show()
    #------------------------------------------------------------------------------------------------------------
    def initializeTWCourtOverView(self):
        self.TWCourtOverView.clear()
        self.db.commit()
        self.TWCourtOverView.setHorizontalHeaderLabels(['编号','类型','校区', '可用状态'])#clear
        
        cmd = 'select * from site;'
        use_status = self.DataBaseExe(cmd)
        n = len(use_status)
        self.TWCourtOverView.setRowCount(n)
        for i in range(n):
            id = use_status[i][0]
            type = use_status[i][1]
            sitearea = use_status[i][2]
            valid = use_status[i][3]
            
            name = self.DataBaseExe('select distinct name_ from area where areaid = "' + sitearea + '";')#name and communicate
                        
            self.TWCourtOverView.setItem(i, 0, QTableWidgetItem(id))#add table item
            self.TWCourtOverView.setItem(i, 1, QTableWidgetItem(type))
            #print(time_sta + " \n" + time_end)
            self.TWCourtOverView.setItem(i, 2, QTableWidgetItem(name[0][0]))
            self.TWCourtOverView.setItem(i, 3, QTableWidgetItem(valid))#add table item
        return
    
    def initializeTWResvOverview(self):
        self.TWResvOverview.clear()
        self.db.commit()
        self.TWResvOverview.setHorizontalHeaderLabels(['场地','起讫时间','预定账户', '用户姓名','联系方式'])#clear
        
        cmd = 'select * from site_reserve;'
        use_status = self.DataBaseExe(cmd)
        n = len(use_status)
        self.TWResvOverview.setRowCount(n)
        for i in range(n):
            siteid = use_status[i][0]
            sitetype = use_status[i][1]
            userid = use_status[i][2]
            time_sta = use_status[i][3]
            time_end = use_status[i][4]
            
            name_tel = self.DataBaseExe('select distinct name, tel from user where id = "' + userid + '";')#name and communicate
            #equipName = self.DataBaseExe('select distinct name from  where id = "' +  + '";')#only one
            #print(equipName[0][0])
            
            self.TWResvOverview.setItem(i, 0, QTableWidgetItem(sitetype + siteid))#add table item
            self.TWResvOverview.setItem(i, 1, QTableWidgetItem(time_sta + " \n" + time_end))
            #print(time_sta + " \n" + time_end)
            self.TWResvOverview.setItem(i, 2, QTableWidgetItem(userid))
            self.TWResvOverview.setItem(i, 3, QTableWidgetItem(name_tel[0][0]))#add table item
            self.TWResvOverview.setItem(i, 4, QTableWidgetItem(name_tel[0][1]))
        return 
    
    def initializeTWServOverview(self):
        self.TWServOverview.clear()
        self.db.commit()
        self.TWServOverview.setHorizontalHeaderLabels(['编号','类型','开始时间', '结束时间', '维护商', '联系方式'])#clear
        
        cmd = 'select * from site_service;'
        use_status = self.DataBaseExe(cmd)
        n = len(use_status)
        self.TWServOverview.setRowCount(n)
        for i in range(n):
            siteid = use_status[i][0]
            sitetype = use_status[i][1]
            time_sta = use_status[i][2]
            time_end = use_status[i][3]
            serviceid = use_status[i][4]
            
            name_tel = self.DataBaseExe('select distinct name, tel from service where id = "' + serviceid + '";')#name and communicate
                        
            self.TWServOverview.setItem(i, 0, QTableWidgetItem(siteid))#add table item
            self.TWServOverview.setItem(i, 1, QTableWidgetItem(sitetype))
            #print(time_sta + " \n" + time_end)
            self.TWServOverview.setItem(i, 2, QTableWidgetItem(time_sta))
            self.TWServOverview.setItem(i, 3, QTableWidgetItem(time_end))
            self.TWServOverview.setItem(i, 4, QTableWidgetItem(name_tel[0][0]))
            self.TWServOverview.setItem(i, 5, QTableWidgetItem(name_tel[0][1]))
            
        return
    
    def initializeCBCourt(self):
        self.db.commit()
        self.CBCourt.clear()
        self.CBCourtType.clear()
        cmd = 'select distinct type from site;'
        types = self.DataBaseExe(cmd)
        for i in types:
            self.CBCourt.addItem(i[0])
            self.CBCourtType.addItem(i[0])
            #print(i[0])
            
    def initializeCBCourtType(self):
        self.db.commit()
        self.CBCourtType.clear()
        cmd = 'select distinct type from site;'
        types = self.DataBaseExe(cmd)
        for i in types:
            self.CBCourtType.addItem(i[0])
        
    
    def initializeCBCourtNum(self):
        self.db.commit()
        self.CBCourtNum.clear()
        self.CBCourtNum_2.clear()
        cmd = 'select distinct id from site where type = "' + self.CBCourt.currentText() + '";'
        nums = self.DataBaseExe(cmd)
        for i in nums:
            self.CBCourtNum.addItem(i[0])
            self.CBCourtNum_2.addItem(i[0])
        return 
    
    def initializeCBCourtNum_2(self):
        self.db.commit()
        self.CBCourtNum_2.clear()
        cmd = 'select distinct id from site where type = "' + self.CBCourtType.currentText() + '";'
        nums = self.DataBaseExe(cmd)
        for i in nums:
            self.CBCourtNum_2.addItem(i[0])
        return 
    
    def initializaCBServer(self):
        self.db.commit()
        self.CBServer.clear()
        cmd = 'select distinct name from service;'
        names = self.DataBaseExe(cmd)
        for i in names:
            self.CBServer.addItem(i[0])
        return
        
    '''def btn_PBRefresh_2(self):    
        self.initializeTWCourtOverView()
        self.initializeTWResvOverview()
        self.initializeTWServOverview()
        return'''
    
    def btn_PBConfirm(self):
        self.db.commit()
        time_sta = str(self.DEStart.date().toPyDate())
        time_end = str(self.DEEnd.date().toPyDate())
        
        if time_end < time_sta:
            QMessageBox.warning(self, '警告', "时间不合法") 
            
        sitetype = self.CBCourt.currentText()
        siteid = self.CBCourtNum.currentText()
        serviceName = self.CBServer.currentText()
        cmd = 'select distinct id from service where name = "' + serviceName + '";'
        serviceId = self.DataBaseExe(cmd)
        cmd = 'insert into site_service values ("'
        cmd1 = siteid + '", "' + sitetype + '", "' 
        cmd2 = time_sta + '", "' + time_end + '", "' + serviceId[0][0] + '");'
        self.cursor.execute(cmd + cmd1 + cmd2)
        self.db.commit()
        self.initializeTWServOverview()
        
        #trigger
        '''cmd = 'update site set valid = "不可用" where id = "' + siteid + '" and type = "' + sitetype + '";'
        self.cursor.execute(cmd)
        self.db.commit()'''
        self.initializeTWCourtOverView()
        
        QMessageBox.information(self, '信息', "添加报修成功")
        return  
    
    def btn_PBEnd(self):
        self.db.commit()
        self.e = courtServiceStatus(self.id, self.db, self.campus)   
        self.e.show()
    
    def btn_PBConfirm_2(self):
        self.db.commit()
        type = self.LECourtType.text()
        if type == "":
            return 
        cmd = 'select id from site where type = "' + type + '";'           
        self.cursor.execute(cmd)
        t = self.cursor.fetchone()
        if t == None:
            cmd = 'insert into site values ("1", "' + type + '", "' + self.campus + '", ' + '"可用");'
            self.cursor.execute(cmd)
            self.db.commit()
            
        else:
            cmd = 'select id from site where type = "' + type + '";'
            nums = self.DataBaseExe(cmd)
            b = 0
            for i in nums:
                if int(i[0]) > b:
                    b = int(i[0])
            b = b + 1
            cmd = 'insert into site values("' + str(b) + '", "' + type + '", "' + self.campus + '", ' + '"可用");'
            self.cursor.execute(cmd)
            self.db.commit()
        self.initializeTWCourtOverView()
        self.initializeCBCourt()  
        self.initializeCBCourtNum()
        QMessageBox.information(self, '信息', "场地添加成功") 
        return
    
    def btn_PBValid(self):
        self.db.commit()
        type = self.CBCourtType.currentText()
        id = self.CBCourtNum_2.currentText()
        cmd = 'update site set valid = "可用" where id = "' + id + '" and type = "' + type + '";'
        self.cursor.execute(cmd)
        self.db.commit()
        self.initializeTWCourtOverView()
        QMessageBox.information(self, '信息', "状态已更改") 
        return
    
    def btn_PBInvalid(self):
        self.db.commit()
        type = self.CBCourtType.currentText()
        id = self.CBCourtNum_2.currentText()
        cmd = 'update site set valid = "不可用" where id = "' + id + '" and type = "' + type + '";'
        self.cursor.execute(cmd)
        self.db.commit()
        self.initializeTWCourtOverView()
        QMessageBox.information(self, '信息', "状态已更改") 
        return
    
    def btn_PBConfirm_4(self):
        self.db.commit()
        name = self.LEBuilderName.text()
        tel = self.LEBuilderCommunicate.text()
        
        if name == "" or tel == "":
            return
        
        ids = self.DataBaseExe('select id from service;')
        num = []
        b = 0
        for i in ids:
            k = i[0].split("SE")
            if int(k[1]) > b:
                b = int(k[1])
        b = b + 1
        newId = "SE" + str(b)
        cmd = 'insert into service values ("' + newId + '", "' + name + '", "' + tel + '");'
        #print(cmd)
        self.cursor.execute(cmd)
        self.db.commit()
        self.initializaCBServer()
        QMessageBox.information(self, '信息', "添加成功") 
        
        return
    
       
if __name__ == '__main__':
    app = QApplication(sys.argv) 
    dlg = managerInterface("m1")
    dlg.show()
    sys.exit(app.exec_())
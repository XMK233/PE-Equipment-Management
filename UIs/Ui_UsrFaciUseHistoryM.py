# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\UsrFaciUseHistoryM.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 328)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 249, 237);")
        self.LWResvRecord = QtWidgets.QListWidget(Form)
        self.LWResvRecord.setGeometry(QtCore.QRect(40, 60, 371, 198))
        self.LWResvRecord.setObjectName("LWResvRecord")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(12)
        item.setFont(font)
        self.LWResvRecord.addItem(item)
        self.PBReturn = QtWidgets.QPushButton(Form)
        self.PBReturn.setGeometry(QtCore.QRect(250, 270, 91, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBReturn.sizePolicy().hasHeightForWidth())
        self.PBReturn.setSizePolicy(sizePolicy)
        self.PBReturn.setMinimumSize(QtCore.QSize(0, 40))
        self.PBReturn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PBReturn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PBReturn.setStyleSheet("font: 9pt \"仿宋\";\n"
"background-color:  qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 173, 69), stop:0.375 rgba(255, 255, 155, 69), stop:0.423533 rgba(254, 255, 156, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 233, 144, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 236, 158, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.PBReturn.setObjectName("PBReturn")
        self.PBRefresh = QtWidgets.QPushButton(Form)
        self.PBRefresh.setGeometry(QtCore.QRect(110, 270, 91, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBRefresh.sizePolicy().hasHeightForWidth())
        self.PBRefresh.setSizePolicy(sizePolicy)
        self.PBRefresh.setMinimumSize(QtCore.QSize(0, 40))
        self.PBRefresh.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PBRefresh.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PBRefresh.setStyleSheet("font: 9pt \"仿宋\";\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 173, 69), stop:0.375 rgba(255, 255, 155, 69), stop:0.423533 rgba(254, 255, 156, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 233, 144, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 236, 158, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))")
        self.PBRefresh.setObjectName("PBRefresh")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 331, 22))
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.PBReturn.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "器材使用记录"))
        __sortingEnabled = self.LWResvRecord.isSortingEnabled()
        self.LWResvRecord.setSortingEnabled(False)
        item = self.LWResvRecord.item(0)
        item.setText(_translate("Form", "初始化"))
        self.LWResvRecord.setSortingEnabled(__sortingEnabled)
        self.PBReturn.setText(_translate("Form", "返回"))
        self.PBRefresh.setText(_translate("Form", "刷新"))
        self.label.setText(_translate("Form", "点击归还"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


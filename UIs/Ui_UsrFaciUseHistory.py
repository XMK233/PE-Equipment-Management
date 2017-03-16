# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\UsrFaciUseHistory.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UsrResvHistory(object):
    def setupUi(self, UsrResvHistory):
        UsrResvHistory.setObjectName("UsrResvHistory")
        UsrResvHistory.resize(468, 290)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UsrResvHistory.setWindowIcon(icon)
        UsrResvHistory.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.verticalLayout = QtWidgets.QVBoxLayout(UsrResvHistory)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(UsrResvHistory)
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.LWResvRecord = QtWidgets.QListWidget(UsrResvHistory)
        self.LWResvRecord.setObjectName("LWResvRecord")
        item = QtWidgets.QListWidgetItem()
        self.LWResvRecord.addItem(item)
        self.verticalLayout.addWidget(self.LWResvRecord)
        self.PBReturn = QtWidgets.QPushButton(UsrResvHistory)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PBReturn.sizePolicy().hasHeightForWidth())
        self.PBReturn.setSizePolicy(sizePolicy)
        self.PBReturn.setMinimumSize(QtCore.QSize(0, 40))
        self.PBReturn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PBReturn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PBReturn.setStyleSheet("font: 9pt \"仿宋\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(168, 168, 168, 255), stop:0.98 rgba(153, 221, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.PBReturn.setObjectName("PBReturn")
        self.verticalLayout.addWidget(self.PBReturn)

        self.retranslateUi(UsrResvHistory)
        self.PBReturn.clicked.connect(UsrResvHistory.close)
        QtCore.QMetaObject.connectSlotsByName(UsrResvHistory)

    def retranslateUi(self, UsrResvHistory):
        _translate = QtCore.QCoreApplication.translate
        UsrResvHistory.setWindowTitle(_translate("UsrResvHistory", "场地预定记录"))
        self.label.setText(_translate("UsrResvHistory", "场地预定记录"))
        __sortingEnabled = self.LWResvRecord.isSortingEnabled()
        self.LWResvRecord.setSortingEnabled(False)
        item = self.LWResvRecord.item(0)
        item.setText(_translate("UsrResvHistory", "初始化"))
        self.LWResvRecord.setSortingEnabled(__sortingEnabled)
        self.PBReturn.setText(_translate("UsrResvHistory", "返回"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UsrResvHistory = QtWidgets.QWidget()
    ui = Ui_UsrResvHistory()
    ui.setupUi(UsrResvHistory)
    UsrResvHistory.show()
    sys.exit(app.exec_())


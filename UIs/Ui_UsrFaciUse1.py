# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\UsrFaciUse1.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UsrFaciUse(object):
    def setupUi(self, UsrFaciUse):
        UsrFaciUse.setObjectName("UsrFaciUse")
        UsrFaciUse.resize(441, 332)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/新前缀/image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UsrFaciUse.setWindowIcon(icon)
        UsrFaciUse.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.verticalLayout = QtWidgets.QVBoxLayout(UsrFaciUse)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(UsrFaciUse)
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.TWFacNumTim = QtWidgets.QTableWidget(UsrFaciUse)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TWFacNumTim.sizePolicy().hasHeightForWidth())
        self.TWFacNumTim.setSizePolicy(sizePolicy)
        self.TWFacNumTim.setMouseTracking(False)
        self.TWFacNumTim.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TWFacNumTim.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TWFacNumTim.setAutoFillBackground(True)
        self.TWFacNumTim.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.TWFacNumTim.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TWFacNumTim.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TWFacNumTim.setLineWidth(1)
        self.TWFacNumTim.setMidLineWidth(0)
        self.TWFacNumTim.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TWFacNumTim.setAlternatingRowColors(False)
        self.TWFacNumTim.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TWFacNumTim.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TWFacNumTim.setIconSize(QtCore.QSize(0, 0))
        self.TWFacNumTim.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TWFacNumTim.setShowGrid(True)
        self.TWFacNumTim.setGridStyle(QtCore.Qt.DashDotLine)
        self.TWFacNumTim.setWordWrap(True)
        self.TWFacNumTim.setCornerButtonEnabled(True)
        self.TWFacNumTim.setObjectName("TWFacNumTim")
        self.TWFacNumTim.setColumnCount(3)
        self.TWFacNumTim.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFacNumTim.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TWFacNumTim.setItem(0, 0, item)
        self.TWFacNumTim.horizontalHeader().setCascadingSectionResizes(False)
        self.TWFacNumTim.horizontalHeader().setDefaultSectionSize(130)
        self.TWFacNumTim.horizontalHeader().setHighlightSections(True)
        self.TWFacNumTim.horizontalHeader().setMinimumSectionSize(30)
        self.TWFacNumTim.horizontalHeader().setSortIndicatorShown(False)
        self.TWFacNumTim.horizontalHeader().setStretchLastSection(False)
        self.TWFacNumTim.verticalHeader().setCascadingSectionResizes(False)
        self.TWFacNumTim.verticalHeader().setDefaultSectionSize(37)
        self.TWFacNumTim.verticalHeader().setHighlightSections(False)
        self.TWFacNumTim.verticalHeader().setSortIndicatorShown(False)
        self.TWFacNumTim.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.TWFacNumTim)
        self.PBReturn = QtWidgets.QPushButton(UsrFaciUse)
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

        self.retranslateUi(UsrFaciUse)
        self.PBReturn.clicked.connect(UsrFaciUse.close)
        QtCore.QMetaObject.connectSlotsByName(UsrFaciUse)

    def retranslateUi(self, UsrFaciUse):
        _translate = QtCore.QCoreApplication.translate
        UsrFaciUse.setWindowTitle(_translate("UsrFaciUse", "器材借用信息"))
        self.label.setText(_translate("UsrFaciUse", "器材借用信息"))
        self.TWFacNumTim.setSortingEnabled(False)
        item = self.TWFacNumTim.verticalHeaderItem(0)
        item.setText(_translate("UsrFaciUse", "1"))
        item = self.TWFacNumTim.verticalHeaderItem(1)
        item.setText(_translate("UsrFaciUse", "2"))
        item = self.TWFacNumTim.verticalHeaderItem(2)
        item.setText(_translate("UsrFaciUse", "3"))
        item = self.TWFacNumTim.verticalHeaderItem(3)
        item.setText(_translate("UsrFaciUse", "4"))
        item = self.TWFacNumTim.verticalHeaderItem(4)
        item.setText(_translate("UsrFaciUse", "5"))
        item = self.TWFacNumTim.horizontalHeaderItem(0)
        item.setText(_translate("UsrFaciUse", "器材"))
        item = self.TWFacNumTim.horizontalHeaderItem(1)
        item.setText(_translate("UsrFaciUse", "数量"))
        item = self.TWFacNumTim.horizontalHeaderItem(2)
        item.setText(_translate("UsrFaciUse", "时间"))
        __sortingEnabled = self.TWFacNumTim.isSortingEnabled()
        self.TWFacNumTim.setSortingEnabled(False)
        self.TWFacNumTim.setSortingEnabled(__sortingEnabled)
        self.PBReturn.setText(_translate("UsrFaciUse", "返回"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UsrFaciUse = QtWidgets.QWidget()
    ui = Ui_UsrFaciUse()
    ui.setupUi(UsrFaciUse)
    UsrFaciUse.show()
    sys.exit(app.exec_())

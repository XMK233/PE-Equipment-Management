# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\FaciBreak.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FaciBreak(object):
    def setupUi(self, FaciBreak):
        FaciBreak.setObjectName("FaciBreak")
        FaciBreak.resize(449, 337)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FaciBreak.setWindowIcon(icon)
        FaciBreak.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FaciBreak)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(FaciBreak)
        self.label.setStyleSheet("font: 75 15pt \"华文楷体\";\n"
"color: rgb(0, 0, 0);")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.TWFaciBreak = QtWidgets.QTableWidget(FaciBreak)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TWFaciBreak.sizePolicy().hasHeightForWidth())
        self.TWFaciBreak.setSizePolicy(sizePolicy)
        self.TWFaciBreak.setMouseTracking(False)
        self.TWFaciBreak.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TWFaciBreak.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TWFaciBreak.setAutoFillBackground(True)
        self.TWFaciBreak.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.TWFaciBreak.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.TWFaciBreak.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TWFaciBreak.setLineWidth(1)
        self.TWFaciBreak.setMidLineWidth(0)
        self.TWFaciBreak.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.TWFaciBreak.setAlternatingRowColors(False)
        self.TWFaciBreak.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TWFaciBreak.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TWFaciBreak.setIconSize(QtCore.QSize(0, 0))
        self.TWFaciBreak.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.TWFaciBreak.setShowGrid(True)
        self.TWFaciBreak.setGridStyle(QtCore.Qt.DashDotLine)
        self.TWFaciBreak.setWordWrap(True)
        self.TWFaciBreak.setCornerButtonEnabled(True)
        self.TWFaciBreak.setObjectName("TWFaciBreak")
        self.TWFaciBreak.setColumnCount(2)
        self.TWFaciBreak.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TWFaciBreak.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TWFaciBreak.setItem(0, 0, item)
        self.TWFaciBreak.horizontalHeader().setCascadingSectionResizes(False)
        self.TWFaciBreak.horizontalHeader().setDefaultSectionSize(200)
        self.TWFaciBreak.horizontalHeader().setHighlightSections(True)
        self.TWFaciBreak.horizontalHeader().setMinimumSectionSize(30)
        self.TWFaciBreak.horizontalHeader().setSortIndicatorShown(False)
        self.TWFaciBreak.horizontalHeader().setStretchLastSection(False)
        self.TWFaciBreak.verticalHeader().setCascadingSectionResizes(False)
        self.TWFaciBreak.verticalHeader().setDefaultSectionSize(37)
        self.TWFaciBreak.verticalHeader().setHighlightSections(False)
        self.TWFaciBreak.verticalHeader().setSortIndicatorShown(False)
        self.TWFaciBreak.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.TWFaciBreak)
        self.PBReturn = QtWidgets.QPushButton(FaciBreak)
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

        self.retranslateUi(FaciBreak)
        self.PBReturn.clicked.connect(FaciBreak.close)
        QtCore.QMetaObject.connectSlotsByName(FaciBreak)

    def retranslateUi(self, FaciBreak):
        _translate = QtCore.QCoreApplication.translate
        FaciBreak.setWindowTitle(_translate("FaciBreak", "器材损坏"))
        self.label.setText(_translate("FaciBreak", "器材损坏信息"))
        self.TWFaciBreak.setSortingEnabled(False)
        item = self.TWFaciBreak.verticalHeaderItem(0)
        item.setText(_translate("FaciBreak", "1"))
        item = self.TWFaciBreak.verticalHeaderItem(1)
        item.setText(_translate("FaciBreak", "2"))
        item = self.TWFaciBreak.verticalHeaderItem(2)
        item.setText(_translate("FaciBreak", "3"))
        item = self.TWFaciBreak.verticalHeaderItem(3)
        item.setText(_translate("FaciBreak", "4"))
        item = self.TWFaciBreak.verticalHeaderItem(4)
        item.setText(_translate("FaciBreak", "5"))
        item = self.TWFaciBreak.horizontalHeaderItem(0)
        item.setText(_translate("FaciBreak", "器材"))
        item = self.TWFaciBreak.horizontalHeaderItem(1)
        item.setText(_translate("FaciBreak", "数量"))
        __sortingEnabled = self.TWFaciBreak.isSortingEnabled()
        self.TWFaciBreak.setSortingEnabled(False)
        self.TWFaciBreak.setSortingEnabled(__sortingEnabled)
        self.PBReturn.setText(_translate("FaciBreak", "返回"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FaciBreak = QtWidgets.QWidget()
    ui = Ui_FaciBreak()
    ui.setupUi(FaciBreak)
    FaciBreak.show()
    sys.exit(app.exec_())


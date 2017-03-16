# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\eclipse mares programs\eric6\dataproject\UserReadMe.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UserReadMe(object):
    def setupUi(self, UserReadMe):
        UserReadMe.setObjectName("UserReadMe")
        UserReadMe.setEnabled(True)
        UserReadMe.resize(400, 340)
        UserReadMe.setMinimumSize(QtCore.QSize(400, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/hλlf-life.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserReadMe.setWindowIcon(icon)
        UserReadMe.setToolTip("")
        UserReadMe.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.widget = QtWidgets.QWidget(UserReadMe)
        self.widget.setGeometry(QtCore.QRect(31, 21, 351, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TBInfo = QtWidgets.QTextBrowser(self.widget)
        self.TBInfo.setStyleSheet("background-color: rgb(235, 255, 253);")
        self.TBInfo.setObjectName("TBInfo")
        self.verticalLayout.addWidget(self.TBInfo)
        self.PBKnown = QtWidgets.QPushButton(self.widget)
        self.PBKnown.setMinimumSize(QtCore.QSize(0, 35))
        self.PBKnown.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(168, 168, 168, 255), stop:0.98 rgba(153, 221, 255, 255), stop:1 rgba(0, 0, 0, 0));")
        self.PBKnown.setObjectName("PBKnown")
        self.verticalLayout.addWidget(self.PBKnown)

        self.retranslateUi(UserReadMe)
        self.PBKnown.clicked.connect(UserReadMe.close)
        QtCore.QMetaObject.connectSlotsByName(UserReadMe)

    def retranslateUi(self, UserReadMe):
        _translate = QtCore.QCoreApplication.translate
        UserReadMe.setWindowTitle(_translate("UserReadMe", "用户须知"))
        self.TBInfo.setHtml(_translate("UserReadMe", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">用户须知：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1. 用户借还器材需在管理员处执行，此软件只为用户提供查询功能。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">2. 用户借用器材，要在体育管理中心关闭之前归还，否则视作损坏。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3. 若损坏器材，请尽早到管理员处解决。</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.PBKnown.setText(_translate("UserReadMe", "知道了"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserReadMe = QtWidgets.QWidget()
    ui = Ui_UserReadMe()
    ui.setupUi(UserReadMe)
    UserReadMe.show()
    sys.exit(app.exec_())


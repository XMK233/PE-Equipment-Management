# -*- coding: utf-8 -*-

"""
Module implementing TabWidget.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTabWidget

from Ui_InquiryWindowSdudent import Ui_TabWidget


class TabWidget(QTabWidget, Ui_TabWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TabWidget, self).__init__(parent)
        self.setupUi(self)

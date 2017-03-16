# -*- coding: utf-8 -*-

"""
Module implementing ManagerInterface.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTabWidget

from Ui_ManagerInterface import Ui_TabWidget


class ManagerInterface(QTabWidget, Ui_TabWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ManagerInterface, self).__init__(parent)
        self.setupUi(self)

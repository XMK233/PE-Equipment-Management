# -*- coding: utf-8 -*-

"""
Module implementing UserReadMe1.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_UserReadMe1 import Ui_UserReadMe1


class UserReadMe1(QWidget, Ui_UserReadMe1):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(UserReadMe1, self).__init__(parent)
        self.setupUi(self)

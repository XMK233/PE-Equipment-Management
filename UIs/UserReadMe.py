# -*- coding: utf-8 -*-

"""
Module implementing UserReadMe.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_UserReadMe import Ui_UserReadMe


class UserReadMe(QWidget, Ui_UserReadMe):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(UserReadMe, self).__init__(parent)
        self.setupUi(self)

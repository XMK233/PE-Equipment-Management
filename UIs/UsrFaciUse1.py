# -*- coding: utf-8 -*-

"""
Module implementing UsrFaciUse.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_UsrFaciUse1 import Ui_UsrFaciUse


class UsrFaciUse(QWidget, Ui_UsrFaciUse):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(UsrFaciUse, self).__init__(parent)
        self.setupUi(self)

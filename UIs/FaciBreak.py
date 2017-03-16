# -*- coding: utf-8 -*-

"""
Module implementing FaciBreak.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_FaciBreak import Ui_FaciBreak


class FaciBreak(QWidget, Ui_FaciBreak):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FaciBreak, self).__init__(parent)
        self.setupUi(self)

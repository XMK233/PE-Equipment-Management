# -*- coding: utf-8 -*-

"""
Module implementing UsrFaciBreakDel.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_UsrFaciBreakDel import Ui_Form


class UsrFaciBreakDel(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(UsrFaciBreakDel, self).__init__(parent)
        self.setupUi(self)

# -*- coding: utf-8 -*-

"""
Module implementing UsrResvHistory.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_UsrResvHistory1 import Ui_Form


class UsrResvHistory(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)

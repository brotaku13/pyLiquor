from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.Cabinet import Cabinet
from Widgets.Search import Search

import sys
import subprocess as sub
import os


class MainWindow(QWidget):
    """Define's the main window of the application
    
    Arguments:
        QWidget {QWidget} -- Inherits from QWidget
    """

    def __init__(self, data_handler, parent=None):
        super(QWidget, self).__init__(parent)
        self.resize(1000, 500)
        self.setWindowTitle("pyCohol")

        self._data_handler = data_handler

        self._app_stack = QStackedWidget()

        self._cabinet_page = Cabinet(self._data_handler)
        self._cabinet_page.setObjectName("cabinet")
        self._cabinet_page.populate()
        self._app_stack.addWidget(self._cabinet_page)

        self._search = Search(self._data_handler)
        self._search.setObjectName("search")
        self._app_stack.addWidget(self._search)

        button_size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_size_policy.setHorizontalStretch(1)
        self._button_cabinet = QPushButton("Cabinet")
        self._button_cabinet.setObjectName("button_cabinet")
        self._button_cabinet.setMaximumHeight(80)
        self._button_cabinet.setMaximumWidth(200)
        self._button_cabinet.setSizePolicy(button_size_policy)
        self._button_cabinet.clicked.connect(lambda: self.switch_page(0))
        
        self._button_search = QPushButton("Search")
        self._button_search.setObjectName("button_search")
        self._button_search.setMaximumHeight(80)
        self._button_search.setMaximumWidth(200)
        self._button_search.setSizePolicy(button_size_policy)
        self._button_search.clicked.connect(lambda: self.switch_page(1))

        self._button_view_data = QPushButton("View Database")
        self._button_view_data.clicked.connect(self.open_data)
        self._button_view_data.setMaximumHeight(80)
        self._button_view_data.setMaximumWidth(200)
        self._button_view_data.setSizePolicy(button_size_policy)

        self.define_layout()

    def define_layout(self):
        """Defines layout of PyLiquor
        """
        grid = QGridLayout()
        grid.setContentsMargins(11, 11, 0, 0)

        grid.addWidget(self._button_cabinet, 0, 0)
        grid.addWidget(self._button_search, 1, 0)
        
        spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)
        grid.addItem(spacer, 3, 0, -1, -1)
        grid.addWidget(self._button_view_data, 2, 0)

        grid.addWidget(self._app_stack, 0, 1, -1, -1)

        grid.setHorizontalSpacing(0)

        self.setLayout(grid)

    def switch_page(self, index):
        """Switches the index of the stacked widget
        
        Arguments:
            index {int} -- index to switch to
        """

        if index == 0:
            self._cabinet_page.populate()
        self._app_stack.setCurrentIndex(index)
        if index == 1:
            self._search.back_to_home()

    def open_data(self):
        if os.name == 'nt':
            sub.run(['cmd', '/c', 'start', 'excel.exe', 'all_data.csv'])
        elif os.name == 'posix':
            sub.run(['libreoffice', '--calc', 'Alcohol_Data/all_data.csv'])


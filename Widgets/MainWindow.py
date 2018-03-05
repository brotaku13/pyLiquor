from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.Cabinet import Cabinet
from Widgets.Search import Search

import sys


class MainWindow(QWidget):

    def __init__(self, data_handler, parent=None):
        super(QWidget, self).__init__(parent)
        self.resize(950, 500)
        self.setWindowTitle("pyCohol")

        self._data_handler = data_handler
        # central Widget is a stacked Widget
        self._app_stack = QStackedWidget()

        self._cabinet_page = Cabinet(self._data_handler)
        self._cabinet_page.setObjectName("cabinet")
        self._app_stack.addWidget(self._cabinet_page)


        self._search = Search(self._data_handler)
        self._search.setObjectName("search")
        self._app_stack.addWidget(self._search)
        self._app_stack.setCurrentIndex(1)


        # buttons
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

        # self._button_recipe = QPushButton("Recipes")
        # self._button_recipe.setObjectName("button_recipes")
        # self._button_recipe.setMaximumHeight(80)
        # self._button_recipe.setMaximumWidth(200)
        # self._button_recipe.setSizePolicy(button_size_policy)

        # self.define_stylesheets()
        self.define_layout()


    def define_layout(self):

        grid = QGridLayout()
        grid.setContentsMargins(11, 11, 0, 0)

        grid.addWidget(self._button_cabinet, 0, 0)
        grid.addWidget(self._button_search, 1, 0)
        #grid.addWidget(self._button_recipe, 2, 0)

        spacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Preferred)
        grid.addItem(spacer, 3, 0, -1, -1)

        grid.addWidget(self._app_stack, 0, 1, -1, -1)

        grid.setHorizontalSpacing(0)

        self.setLayout(grid)

    def switch_page(self, index):
        self._app_stack.setCurrentIndex(index)


# app = QApplication(sys.argv)
# mainWindow = MainWindow()
# mainWindow.show()
# sys.exit(app.exec_())
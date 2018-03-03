from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.Search_Widgets.Home import Home
from Widgets.Search_Widgets.Results import Results
class Search(QWidget):

    def __init__(self, parent=None):
        super(Search, self).__init__(parent)

        self._search_apps = QStackedWidget()

        self._home = Home()
        self._home.search_action.connect(self.switch_page)
        self._search_apps.addWidget(self._home)

        self._search_results = Results()
        self._search_apps.addWidget(self._search_results)

        self.define_layout()

    @pyqtSlot(str)
    def switch_page(self, search_arg):
        self._search_results.populate(search_arg)
        self._search_apps.setCurrentIndex(1)
        print(search_arg)

    def define_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(self._search_apps)
        self.setLayout(layout)


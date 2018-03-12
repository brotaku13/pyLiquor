from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.Search_Widgets.Home import Home
from Widgets.Search_Widgets.Results import Results


class Search(QWidget):
    """Container class for the search widgets
    
    Arguments:
        QWidget {QWidget} -- inherits from QWidget
    """

    def __init__(self, data_handler, parent=None):
        super(Search, self).__init__(parent)
        self._data_handler = data_handler
        self._search_apps = QStackedWidget()
        
        self._home = Home()
        self._home.search_action.connect(self.search)
        self._search_apps.addWidget(self._home)

        self._search_results = Results()
        self._search_results.back_to_search.connect(self.back_to_home)
        self._search_apps.addWidget(self._search_results)

        self.define_layout()

    @pyqtSlot(str)
    def search(self, search_arg):
        """Performs the search
        
        Arguments:
            search_arg {str} -- the search arguments given by the user
        """

        self._search_results.populate(self._data_handler, search_arg)
        self._search_apps.setCurrentIndex(1)
        print(search_arg)

    @pyqtSlot()
    def back_to_home(self):
        """back button functionality-goes back to home of search page
        """

        self._search_apps.setCurrentIndex(0)

    def define_layout(self):
        """defines the layout
        """

        layout = QHBoxLayout()
        layout.addWidget(self._search_apps)
        layout.setContentsMargins(11, 0, 11, 20)
        self.setLayout(layout)


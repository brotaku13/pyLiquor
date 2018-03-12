from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LiquorView(QTreeWidget):
    """Displays the liquor in a list format
    
    Arguments:
        QTreeWidget {QTreeWidget} -- Inherits from QTreeWidget
    """

    def __init__(self, categories, parent=None):
        super(LiquorView, self).__init__(parent)
        self.setColumnCount(len(categories))
        self.resizeColumnToContents(0)
        self.setMaximumWidth(500)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)
        self.setHeaderLabels(categories)
        table_size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setSizePolicy(table_size_policy)
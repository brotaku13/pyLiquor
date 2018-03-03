from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LiquorView(QTreeWidget):

    def __init__(self, categories, parent=None):
        super(LiquorView, self).__init__(parent)

        self.setColumnCount(len(categories))
        self.setMaximumWidth(500)
        self.setSortingEnabled(True)
        self.setHeaderLabels(categories)



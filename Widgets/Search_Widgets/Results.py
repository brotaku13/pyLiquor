from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.LiquorDetails import LiquorDetails
from Widgets.LiquorView import LiquorView

class Results(QWidget):

    def __init__(self, parent=None):
        super(Results, self).__init__(parent)

        self._details_view = LiquorDetails()
        self._liquor_view = LiquorView(["Name"])

        self._button_back = QPushButton("Back")
        self._add_to_cabinet = QPushButton("Add to Cabinet")

        self.define_layout()

    def populate(self, search_args):
        if search_args == 'wine':
            pass
        # etc....

    def define_layout(self):
        left = QVBoxLayout()
        button_bar = QHBoxLayout()
        button_bar.addWidget(self._button_back)
        button_bar.addWidget(self._add_to_cabinet)

        left.addWidget(self._liquor_view)
        left.addLayout(button_bar)

        layout = QHBoxLayout()

        layout.addLayout(left)
        layout.addWidget(self._details_view)
        self.setLayout(layout)



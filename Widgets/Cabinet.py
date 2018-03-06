from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.LiquorDetails import CabinetLiquorDetails
from Widgets.LiquorView import LiquorView


class Cabinet(QWidget):

    def __init__(self, data_handler, parent=None):
        super(Cabinet, self).__init__(parent)

        self._radiobutton_current = QRadioButton("Current")
        self._radiobutton_all = QRadioButton("All")

        self._collection_view = LiquorView(["Name", "Type", "Amount"])
        
        self._details_view = CabinetLiquorDetails()

        self.define_layout()

    def define_layout(self):
        layout_cabinet = QHBoxLayout()
        layout_cabinet.setContentsMargins(11, 0, 11, 20)


        layout_filter_buttons = QHBoxLayout()
        layout_filter_buttons.addWidget(self._radiobutton_current)
        layout_filter_buttons.addWidget(self._radiobutton_all)
        spacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout_filter_buttons.addItem(spacer)

        layout_treeview = QVBoxLayout()
        layout_treeview.setContentsMargins(0, 0, 11, 11)
        layout_treeview.addWidget(self._collection_view)
        layout_treeview.addLayout(layout_filter_buttons)

        layout_cabinet.addLayout(layout_treeview)
        layout_cabinet.addWidget(self._details_view)

        self.setLayout(layout_cabinet)





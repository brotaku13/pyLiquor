from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.LiquorDetails import SearchLiquorDetails
from Widgets.LiquorView import LiquorView
from Widgets.Search_Widgets.LiquorViewItem import LiquorViewItem


class Results(QWidget):
    
    back_to_search = pyqtSignal()

    def __init__(self, parent=None):
        super(Results, self).__init__(parent)

        self._details_view = SearchLiquorDetails()
        self._liquor_view = LiquorView(["Name", "type"])
        self._liquor_view.setColumnWidth(0, 400)
        self._liquor_view.currentItemChanged.connect(self.update_details)
        
        self._button_back = QPushButton("Back")
        self._button_back.clicked.connect(self.on_back_clicked)

        self._details_view.add_to_cabinet.connect(self.add_item_to_cabinet)

        self.define_layout()

    def on_back_clicked(self):
        #self.clear_tree()
        self.back_to_search.emit()

    def update_details(self, current_liquor_item: LiquorViewItem):
        if current_liquor_item is not None:
            self._details_view.update_ui(current_liquor_item)

    def populate(self, data_handler, search_args):
        self.clear_tree()
        if search_args == 'wine':
            for entry in data_handler.get_wine():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'beer':
            for entry in data_handler.get_beer():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'spirits':
            for entry in data_handler.get_spirits():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'coolers':
            for entry in data_handler.get_coolers():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'cider':
            for entry in data_handler.get_cider():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'liqueur':
            for entry in data_handler.get_liqour():
                self._liquor_view.addTopLevelItem(entry)
        elif search_args == 'sake':
            for entry in data_handler.get_sake():
                self._liquor_view.addTopLevelItem(entry)
    @pyqtSlot()
    def add_item_to_cabinet(self):
        liquor_to_add = self._liquor_view.selectedItems()
        for item in liquor_to_add:
            print(item)
        # : returns QTreeWidgetItem

    def clear_tree(self):
        for i in reversed(range(self._liquor_view.topLevelItemCount())):
            self._liquor_view.takeTopLevelItem(i) 

    def define_layout(self):
        left = QVBoxLayout()
        button_bar = QHBoxLayout()
        button_bar.addWidget(self._button_back)
        button_bar.setAlignment(Qt.AlignLeft)

        left.addWidget(self._liquor_view)
        left.addLayout(button_bar)

        layout = QHBoxLayout()

        layout.addLayout(left)
        layout.addWidget(self._details_view)
        layout.setContentsMargins(0, 0, 0, 11)
        self.setLayout(layout)



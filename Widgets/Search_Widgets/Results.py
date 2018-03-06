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
        self._liquor_view = LiquorView(["Name"])
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
                item = LiquorViewItem(entry['ID'],
                                        entry['Name'].replace('\'', ''),
                                        entry['Maker'],
                                        entry['Category'], 
                                        entry['Sub_Category'], 
                                        entry['Sub_Sub_Category'],
                                        entry['Sub_Sub_Sub_Category'],
                                        float(entry['Cost']),
                                        float(entry['Volume(ml)']),
                                        float(entry['Alcohol_By_Volume']),
                                        entry['Aroma'],
                                        entry['Color'],
                                        entry['Origin'],
                                        entry['Region'])
                item.setText(0, item.get_name().title())
                self._liquor_view.addTopLevelItem(item)

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



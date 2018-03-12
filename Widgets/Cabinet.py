from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd
import csv

from Widgets.LiquorDetails import CabinetLiquorDetails
from Widgets.LiquorView import LiquorView
from Widgets.Search_Widgets import LiquorViewItem


class Cabinet(QWidget):
    """Display's the contents of the user's cabinet as well as any details about the contents
    
    Arguments:
        QWidget {QWidget} -- Inherits from QWidget class
    """

    def __init__(self, data_handler, parent=None):
        super(Cabinet, self).__init__(parent)
        self._data_handler = data_handler
        self._collection_view = LiquorView(["Name", "Type", "Quantity"])
        self._collection_view.currentItemChanged.connect(self.update_details)
        self._collection_view.setColumnWidth(0, 325)
        self._details_view = CabinetLiquorDetails()
        self._details_view.remove_from_cabinet.connect(self.remove_from_cabinet)
        self.define_layout()

    @pyqtSlot()
    def remove_from_cabinet(self):
        """Removes currently highlighted item from the user's cabinet or decrements if Quantity > 1
        """

        item = self._collection_view.currentItem()
        if item is not None:
            
            with open('Alcohol_Data/cabinet.csv', 'r', newline='') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                data = list(reader)
            with open('Alcohol_Data/cabinet.csv', 'w', newline='') as f:
                writer = csv.DictWriter(f, headers)
                writer.writeheader()
                for row in data:
                    if row['ID'] == str(item.get_id()):
                        if float(row['Quantity']) > 1:
                            row['Quantity'] = str(float(row['Quantity']) - 1)
                            writer.writerow(row)
                    else:
                        writer.writerow(row)
            self.populate()

    def update_details(self, current_liquor_item: LiquorViewItem):
        """Update's the details view with the details of the currently selected item
        
        Arguments:
            current_liquor_item {LiquorViewItem} -- The currently highlighted item from the QTreeWidget
        """

        if current_liquor_item is not None:
            self._details_view.update_ui(current_liquor_item)

    def populate(self):
        """Populates the QTreeView with items from the user's cabinet CSV
        """

        self.clear_tree()
        for entry in self._data_handler.get_cabinet():
            self._collection_view.addTopLevelItem(entry)
    
    def clear_tree(self):
        """clears the QTreeWidget of items. Used when updating the contents
        """

        for i in reversed(range(self._collection_view.topLevelItemCount())):
            self._collection_view.takeTopLevelItem(i) 

    def define_layout(self):
        """Define's alyout of widget
        """

        layout_cabinet = QHBoxLayout()
        layout_cabinet.setContentsMargins(11, 0, 11, 20)

        layout_filter_buttons = QHBoxLayout()
        spacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout_filter_buttons.addItem(spacer)

        layout_treeview = QVBoxLayout()
        layout_treeview.setContentsMargins(0, 0, 11, 11)
        layout_treeview.addWidget(self._collection_view)
        layout_treeview.addLayout(layout_filter_buttons)

        layout_cabinet.addLayout(layout_treeview)
        layout_cabinet.addWidget(self._details_view)

        self.setLayout(layout_cabinet)

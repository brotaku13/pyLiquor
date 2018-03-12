from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Widgets.LiquorDetails import SearchLiquorDetails
from Widgets.LiquorView import LiquorView
from Widgets.Search_Widgets.LiquorViewItem import LiquorViewItem
from Data_Handler import Data_Handler
import pandas as pd
import numpy as np
import csv


class Results(QWidget):
    """Results page for the search widget
    
    Arguments:
        QWidget {QWidget} -- Inherits from QWidget
    """

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
        """Emits the back_to_search signal when the back button is clicked
        """
        self.back_to_search.emit()

    def update_details(self, current_liquor_item: LiquorViewItem):
        """Updates the details in the liquor details view. 
        
        Arguments:
            current_liquor_item {LiquorViewItem} -- The item that is currently highlighted in the QTreeView
        """

        if current_liquor_item is not None:
            self._details_view.update_ui(current_liquor_item)

    def populate(self, data_handler, search_args):
        """Populates the QTreeView with items from the CSV's that match the user's criteria
        
        Arguments:
            data_handler {Data_Handler} -- The data handler singleton responsible for handling the interface betwen the UI and the CSV data
            search_args {str} -- The arguments to be searched for
        """

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
        else:
            for entry in data_handler.search(search_args):
                self._liquor_view.addTopLevelItem(entry)
                
    @pyqtSlot()
    def add_item_to_cabinet(self):
        """Adds the currently highlighted item to the user's cabinet and updates the cabinet list
        """
        file_name = 'Alcohol_Data/cabinet.csv'
        liquor = self._liquor_view.currentItem()
        found = False
        data_handler = Data_Handler()
        user_cabinet = data_handler.get_cabinet()
        for item in user_cabinet:
            if liquor.get_id() == item.get_id():
                found = True
                with open(file_name, 'r', newline='') as file:
                    self._cab = pd.read_csv(file)
                    counter = 0
                    for elem in self._cab['ID']:
                        if elem != liquor.get_id():
                            counter += 1
                        else:
                            break

                    temp_quant = int(self._cab['Quantity'][counter]) + 1
                    #self._cab.loc[:,('Quantity',counter)] = temp_quant
                    temp_df = pd.DataFrame({'Quantity': [temp_quant]}, index=[counter])
                    self._cab.update(temp_df)                 
                    # reader = csv.DictReader(file)
                    # headers = reader.fieldnames
                    # for row in reader:
                    #     print(liquor.get_id())
                    #     print(row['ID'])
                    #     if liquor.get_id() == int(row['ID']):
                    #         temp = int(row['Quantity'])
        if found:
            with open(file_name, 'w', newline='') as file:
                self._cab.to_csv(file, index=False)

        else:
            with open(file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([liquor.get_id(), liquor.get_name(), liquor.get_maker(), liquor.get_category(), liquor.get_sub_category(),
                                liquor.get_sub_sub_category(), liquor.get_sub_sub_sub_category(), liquor.get_cost(), liquor.get_volume(), 
                                liquor.get_abv(), liquor.get_aroma(), liquor.get_color(), "Null", liquor.get_origin(), liquor.get_region(), "1"])

    def clear_tree(self):
        """Clears the current tree's items
        """

        for i in reversed(range(self._liquor_view.topLevelItemCount())):
            self._liquor_view.takeTopLevelItem(i) 

    def define_layout(self):
        """Defines the Widget's layout
        """

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

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LiquorViewItem(QTreeWidgetItem):
    """"Alcohol" class of which is displayed in the LiquorView item
    
    Arguments:
        QTreeWidgetItem {QTreeWidgetItem} -- Inherits from QTreeViewItem
    """

    def __init__(self, ID: int, name: str, maker: str, category: str, sub_category: str, 
                sub_sub_category: str, sub_sub_sub_category: str, cost: float,
                volume: float, alcohol_by_volume: float, aroma: str, color: str, 
                origin: str, region: str):
        self._id = ID
        self._name = name
        self._category = category
        self._maker = maker
        self._sub_category = sub_category
        self._sub_sub_category = sub_sub_category
        self._sub_sub_sub_category = sub_sub_sub_category
        self._cost = cost
        self._volume = volume
        self._alcohol_by_volume = alcohol_by_volume
        self._aroma = aroma
        self._color = color
        self._origin = origin
        self._region = region

        super(QTreeWidgetItem, self).__init__()

    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def get_maker(self):
        return self._maker
    
    def get_category(self):
        return self._category

    def get_sub_category(self):
        return self._sub_category

    def get_sub_sub_category(self):
        return self._sub_sub_category

    def get_sub_sub_sub_category(self):
        return self._sub_sub_sub_category

    def get_cost(self):
        return self._cost
    
    def get_volume(self):
        return self._volume

    def get_abv(self):
        return self._alcohol_by_volume

    def get_aroma(self):
        return self._aroma
    
    def get_color(self):
        return self._color

    def get_origin(self):
        return self._origin

    def get_region(self):
        return self._region

    def __str__(self):
        return "ID: {}, NAME: {}".format(self._id, self._name)
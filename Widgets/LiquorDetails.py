from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from collections import OrderedDict
import math
import webbrowser
import os
import subprocess as sub


class LiquorDetails(QWidget):
    
    add_to_cabinet = pyqtSignal()
    remove_from_cabinet = pyqtSignal()

    def __init__(self, parent=None):
        super(LiquorDetails, self).__init__(parent)

        self._button_buy = QPushButton("Buy Near Me")
        self._button_buy.clicked.connect(self.near_me)    
        
        self.setMinimumWidth(270)
        self.setMaximumWidth(270)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred))
        self._name = QLabel()
        font_name = QFont("Helvetica", 14, 4)
        self._name.setFont(font_name)
        self._name.setWordWrap(True)
        self._name.setAlignment(Qt.AlignCenter)

        font_details = QFont("Helvetica", 12, 1)
        self._maker = QLabel()
        self._category = QLabel()
        self._origin = QLabel()
        self._region = QLabel()
        self._volume = QLabel()
        self._abv = QLabel()
        self._aroma = QLabel()
        self._color = QLabel()

        self.labels = [self._category, self._origin, self._region, self._volume, self._abv, self._aroma, self._color]
        for label in self.labels:
            label.setFont(font_details)

    def near_me(self):
        self.new_search = NearMe()
        self.new_search.setGeometry(QRect(1100,600,400,200))
        self.new_search.show()

    def is_nan(self, x):
        return isinstance(x, float) and math.isnan(x)

    def set_name(self, name):
        self._name.setText(name)

    def set_maker(self, maker):
        if maker != '' and not self.is_nan(maker):
            self._maker.setText(maker)
        else:
            self._maker.setText('')
    
    def set_category(self, *args):
        categories = OrderedDict()
        for word in args:
            if not self.is_nan(word) and word.lower() != 'other' and word.lower() != 'none' and word != '':
                categories[word] = word
        temp = ''
        for i, key in enumerate(list(categories)):
            if i == 0:
                temp = '{}'.format(key)
            elif i == 1:
                temp += ', {}\n'.format(key)
            elif i == 2:
                temp += '{}'.format(key)
            else:
                temp += ', {}'.format(key)
                
        # Get rid of other unesseccary garbage.
        final_word = ''
        count = 0

        # Check size then concatinates for solo word.
        if temp[:4] == 'WINE' or temp[:4] == "BEER" or temp[:4] == "SAKE":
            for char in temp:
                if count != 4:
                    final_word += char
                    count += 1
        elif temp[:5] == "CIDER":
            for char in temp:
                if count != 5:
                    final_word += char
                    count += 1
        elif temp[:6] == "LIQUER" or temp[:6] == "COOLER":
            for char in temp:
                if count != 6:
                    final_word += char
                    count += 1
        elif temp[:7] == "SPIRITS":
            for char in temp:
                if count != 7:
                    final_word += char
                    count += 1

        # Give the final word a title font
        final_word = final_word.title()
        
        self._category.setText(final_word)
    
    def set_origin(self, origin):
        if origin != '' and not self.is_nan(origin):
            self._origin.setText('Origin: {}'.format(origin.title()))
        else:
            self._origin.setText('Origin: N/A')
    
    def set_region(self, region):
        if region != '' and not self.is_nan(region):
            self._region.setText('Region: {}'.format(region.title()))
        else:
            self._region.setText('Region: N/A')
    
    def set_volume(self, volume):
        if volume != '' and not self.is_nan(volume):
            self._volume.setText('Volume (ml): {:.2f}ml'.format(volume))
        else:
            self._volume.setText('Volume (ml): N/A')
    
    def set_abv(self, abv):
        if abv != '' and not self.is_nan(abv):
            self._abv.setText('ABV%: {}'.format(abv))
        else:
            self._abv.setText('ABV%: N/A')
    
    def set_aroma(self, aroma):
        if aroma != '' and not self.is_nan(aroma):
            self._aroma.setText('Aroma: {}'.format(aroma))
        else:
            self._aroma.setText('Aroma: N/A')

    def set_color(self, color):
        if color != '' and not self.is_nan(color):
            self._color.setText('Color: {}'.format(color.title()))
        else:
            self._color.setText('Color: N/A')
    
    def update_ui(self, liquor):
        self.set_name(liquor.get_name())
        self.set_maker(liquor.get_maker())
        self.set_category(liquor.get_category(), liquor.get_sub_category(), 
                            liquor.get_sub_sub_category(), liquor.get_sub_sub_sub_category())
        self.set_origin(liquor.get_origin())
        self.set_region(liquor.get_region())
        self.set_volume(liquor.get_volume())
        self.set_abv(liquor.get_abv())
        self.set_aroma(liquor.get_aroma())
        self.set_color(liquor.get_color())
            

class SearchLiquorDetails(LiquorDetails):
    def __init__(self):
        
        self._button_add_to_cabinet = QPushButton("Add to Cabinet")
        self._button_add_to_cabinet.clicked.connect(self.add_selection)
        super(SearchLiquorDetails, self).__init__()
        self.define_layout()

    def add_selection(self):
        self.add_to_cabinet.emit()
        
    def define_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self._name)
        for widget in self.labels:
            layout.addWidget(widget)

        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addItem(spacer)

        layout.addWidget(self._button_add_to_cabinet)
        layout.addWidget(self._button_buy)

        self.setLayout(layout)


class CabinetLiquorDetails(LiquorDetails):
    def __init__(self):
        super(CabinetLiquorDetails, self).__init__()
        self._button_remove_from_cabinet = QPushButton("Remove from Cabinet")
        self._button_remove_from_cabinet.clicked.connect(self.remove_selection)
        self.define_layout()

    def remove_selection(self):
        self.remove_from_cabinet.emit()
        
    def define_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self._name)
        for widget in self.labels:
            layout.addWidget(widget)

        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addItem(spacer)

        layout.addWidget(self._button_remove_from_cabinet)
        layout.addWidget(self._button_buy)

        self.setLayout(layout)

class NearMe(QWidget):
    def __init__(self, parent=None):
        super(NearMe, self).__init__(parent)
        self.define_layout()

    def define_layout(self):
        self.pop_up = QVBoxLayout()
        self.drop_down = QComboBox()
        self.text = QLabel("What would you like to search for?")
        self.drop_down.addItems(["Liquor Store", "Grocery Store", "Wine", "Other"])
        self.button_search = QPushButton("Search Maps")
        self.button_search.clicked.connect(self.search_maps)
        self.pop_up.addWidget(self.text)
        self.pop_up.addWidget(self.drop_down)
        self.pop_up.addWidget(self.button_search)
        self.setLayout(self.pop_up)
        self.setWindowTitle("Search Near Me")
        
    def search_maps(self):
        go = True
        entry = self.drop_down.currentText()
        if entry == "Other":
            user, ok = QInputDialog.getText(self, "Search Entry", "Enter your search:")
            if ok:
                entry = user
            else:
                go = False
        if go:
            url = 'google.com/maps/search/' + entry.lower() + '/'
            browser = webbrowser.get('google-chrome')
            if os.name == 'nt':
                sub.run(['cmd', '/c', 'start', 'chrome.exe', url])
            elif os.name == 'posix':
                sub.run(['google-chrome', url])

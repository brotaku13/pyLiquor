from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from collections import OrderedDict
import webbrowser
import math
import os
import subprocess as sub


class LiquorDetails(QWidget):
    
    add_to_cabinet = pyqtSignal()

    def __init__(self, parent=None):
        super(LiquorDetails, self).__init__(parent)
        
        self._button_buy = QPushButton("Buy Near Me")
        self._button_buy.clicked.connect(self.near_me)
        self.setMaximumWidth(250)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred))

        self._name = QLabel("Liquor Name here")
        font_name = QFont("Helvetica", 16, 3)
        self._name.setFont(font_name)
        self._name.setWordWrap(True)
        self._name.setAlignment(Qt.AlignCenter)

        font_details = QFont("Helvetica", 12, 1)
        self._maker = QLabel("makers name")
        self._category = QLabel("Category here in [], []\n[], [] format")
        self._origin = QLabel("Origin: []")
        self._region = QLabel("Region: []")
        self._volume = QLabel("Volume: []")
        self._abv = QLabel("ABV%: []")
        self._aroma = QLabel("Aroma: []")
        self._color = QLabel("Color: []")

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
        self._category.setText(temp)
    
    def set_origin(self, origin):
        if origin != '' and not self.is_nan(origin):
            self._origin.setText('Origin: {}'.format(origin))
        else:
            self._origin.setText('Origin: ')
    
    def set_region(self, region):
        if region != '' and not self.is_nan(region):
            self._region.setText('Region: {}'.format(region))
        else:
            self._region.setText('Region: ')
    
    def set_volume(self, volume):
        if volume != '' and not self.is_nan(volume):
            self._volume.setText('Volume (ml): {:.2f}ml'.format(volume))
        else:
            self._volume.setText('Volume (ml): ')
    
    def set_abv(self, abv):
        if abv != '' and not self.is_nan(abv):
            self._abv.setText('ABV%: {}'.format(abv))
        else:
            self._abv.setText('ABV%: ')
    
    def set_aroma(self, aroma):
        if aroma != '' and not self.is_nan(aroma):
            self._aroma.setText('Aroma: {}'.format(aroma))
        else:
            self._aroma.setText('Aroma: ')

    def set_color(self, color):
        if color != '' and not self.is_nan(color):
            self._color.setText('Color: {}'.format(color))
        else:
            self._color.setText('Color: ')
    
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
        self.define_layout()
        
    def define_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self._name)
        for widget in self.labels:
            layout.addWidget(widget)

        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)
        layout.addItem(spacer)

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
                    #not sure on this line, can't personally test
                    sub.run(['chrome', url])
                    #backup plan
                    #browser.open(url, new=2)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from collections import OrderedDict


class LiquorDetails(QWidget):
    
    add_to_cabinet = pyqtSignal()

    def __init__(self, parent=None):
        super(LiquorDetails, self).__init__(parent)
        
        self._button_buy = QPushButton("Buy Near Me")

        self._name = QLabel("Liquor Name here")
        font_name = QFont("Helvetica", 20, 3)
        self._name.setFont(font_name)
        self._name.setWordWrap(True)
        self._name.setAlignment(Qt.AlignCenter)

        font_details = QFont("Helvetica", 14, 2)
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

    def set_name(self, name):
        self._name.setText(name)

    def set_maker(self, maker):
        if maker != '':
            self._maker.show()
            self._maker.setText(maker)
        else:
            self._maker.hide()

    def set_category(self, *args):
        categories = OrderedDict()
        for word in args:
            if word.lower() != 'other' and word.lower() != 'none' and word != '':
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
        if origin != '':
            self._origin.show()
            self._origin.setText('Origin: {}'.format(origin))
        else:
            self._origin.hide()
    
    def set_region(self, region):
        if region != '':
            self._region.show()
            self._region.setText('Region: {}'.format(region))
        else:
            self._region.hide()
    
    def set_volume(self, volume):
        if volume != '':
            self._volume.show()
            self._volume.setText('Volume (ml): {}'.format(volume))
        else:
            self._volume.hide()
    
    def set_abv(self, abv):
        if abv != '':
            self._abv.show()
            self._abv.setText('ABV%: {}'.format(abv))
        else:
            self._abv.hide()
    
    def set_aroma(self, aroma):
        if aroma != '':
            self._aroma.show()
            self._aroma.setText('Aroma: {}'.format(aroma))
        else:
            self._aroma.hide()

    def set_color(self, color):
        if color != '':
            self._color.show()
            self.color.setText('Color: {}'.format(color))
        else:
            self._color.hide()
            

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
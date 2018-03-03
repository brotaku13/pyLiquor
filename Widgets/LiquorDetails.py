from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LiquorDetails(QWidget):

    def __init__(self, parent=None):
        super(LiquorDetails, self).__init__(parent)


        self._name = QLabel("Liquor Name here")
        font_name = QFont("Helvetica", 24, 4)
        self._name.setFont(font_name)
        self._name.setWordWrap(True)
        self._name.setAlignment(Qt.AlignCenter)


        font_details = QFont("Helvetica", 14, 2)

        self._label_type = QLabel("Type:")
        self._label_type.setFont(font_details)
        self._type = QLabel("Type here")
        self._type.setFont(font_details)


        self._label_origin = QLabel("Origin:")
        self._label_origin.setFont(font_details)
        self._origin = QLabel("Origin here")
        self._origin.setFont(font_details)

        self._label_region = QLabel("Region:")
        self._label_region.setFont(font_details)
        self._region = QLabel("Region here")
        self._region.setFont(font_details)

        self._label_supplier = QLabel("Supplier")
        self._label_supplier.setFont(font_details)
        self._supplier = QLabel("Supplier here")
        self._supplier.setFont(font_details)

        self._label_abv = QLabel("Alcohol%")
        self._label_abv.setFont(font_details)
        self._abv = QLabel("abv% here")
        self._abv.setFont(font_details)

        self._button_buy = QPushButton("Buy Near Me")

        self.define_layout()

    def define_layout(self):
        grid = QGridLayout()

        grid.addWidget(self._name, 0, 0, 2, 2, alignment=Qt.AlignCenter)

        grid.addWidget(self._label_type, 2, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self._type, 2, 1, alignment=Qt.AlignRight)

        grid.addWidget(self._label_abv, 3, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self._abv, 3, 1, alignment=Qt.AlignRight)

        grid.addWidget(self._label_origin, 4, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self._origin, 4, 1, alignment=Qt.AlignRight)

        grid.addWidget(self._label_region, 5, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self._region, 5, 1, alignment=Qt.AlignRight)

        grid.addWidget(self._label_supplier, 6, 0, alignment=Qt.AlignLeft)
        grid.addWidget(self._supplier, 6, 1, alignment=Qt.AlignRight)

        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)
        grid.addItem(spacer, 7, 0)

        grid.addWidget(self._button_buy, 8, 0, 1, 2)

        self.setLayout(grid)

    def set_name(self, text):
        self._name.setText(text)

    def set_type(self, text):
        self._type.setText(text)

    def set_origin(self, text):
        self._origin.setText(text)

    def set_region(self, text):
        self._region.setText(text)

    def set_supplier(self, text):
        self._supplier.setText(text)

    def set_abv(self, abv: float):
        self._abv.setText("{}% alc/vol".format(abv))


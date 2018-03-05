from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pathlib import Path


class Home(QWidget):

    search_action = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Home, self).__init__(parent)

        icon_path = Path.cwd() / Path("Resources") / Path("Icons")

        font_browse = QFont("Helvetica", 12, 1)

        self._wine = QToolButton()
        self._wine.setText("Wine")
        self._wine.clicked.connect(lambda: self.on_choose_action("wine"))

        self._beer = QToolButton()
        self._beer.setText("Beer")
        self._beer.clicked.connect(lambda: self.on_choose_action("beer"))

        self._spirits = QToolButton()
        self._spirits.setText("Spirits")
        self._spirits.clicked.connect(lambda: self.on_choose_action("spirits"))

        self._liqeurs = QToolButton()
        self._liqeurs.setText("Liqueur")
        self._liqeurs.clicked.connect(lambda: self.on_choose_action("liqueur"))

        self._cooler = QToolButton()
        self._cooler.setText("Coolers")
        self._cooler.clicked.connect(lambda: self.on_choose_action("coolers"))

        self._cider = QToolButton()
        self._cider.setText("Cider")
        self._cider.clicked.connect(lambda: self.on_choose_action("cider"))

        self._sake = QToolButton()
        self._sake.setText("Sake")
        self._sake.clicked.connect(lambda: self.on_choose_action("sake"))

        self._non_alcoholic = QToolButton()
        self._non_alcoholic.setText("Non-Alcoholic")
        self._non_alcoholic.clicked.connect(lambda: self.on_choose_action("non-alcoholic"))

        button_list = [self._wine, self._beer,
                       self._spirits, self._liqeurs,
                       self._cooler, self._cider,
                       self._sake, self._non_alcoholic]

        button_size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for button in button_list:
            icon = QIcon(str(icon_path / Path('{}.png'.format(button.text().lower()))))
            button.setIcon(icon)
            button.setIconSize(QSize(40, 40))
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            button.setFont(font_browse)
            button.setMaximumHeight(100)
            button.setSizePolicy(button_size_policy)

        self._search_box = QLineEdit()
        self._search_box.returnPressed.connect(lambda: self.on_choose_action(self._search_box.text()))
        self._search_box.setPlaceholderText("Search")
        self._search_box.setMaximumWidth(400)

        self.define_layout()

    # emit signal
    def on_choose_action(self, search_args):
        self.search_action.emit(search_args)

    def define_layout(self):

        browse_layout = QVBoxLayout()
        browse_layout.setContentsMargins(20, 0, 20, 0)

        grid = QGridLayout()
        grid.addWidget(self._wine, 0, 0)
        grid.addWidget(self._beer, 0, 1)
        grid.addWidget(self._spirits, 0, 2)
        grid.addWidget(self._liqeurs, 0, 3)

        grid.addWidget(self._cooler, 1, 0)
        grid.addWidget(self._cider, 1, 1)
        grid.addWidget(self._sake, 1, 2)
        grid.addWidget(self._non_alcoholic, 1, 3)

        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(10)

        search_bar = QHBoxLayout()
        search_bar.addWidget(self._search_box)


        browse_layout.addLayout(search_bar)
        browse_layout.addLayout(grid)

        self.setLayout(browse_layout)




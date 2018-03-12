from PyQt5.QtWidgets import *

from Widgets.MainWindow import MainWindow
from Data_Handler import Data_Handler

import sys
from pathlib import Path


def check_filesystem():
    checl = True

    cwd = Path.cwd()
    widgets = cwd / Path('Widgets')
    search_widgets = widgets / Path('Search_Widgets')

    home = search_widgets / Path('Home.py')
    liquorviewitem = search_widgets / Path('LiquorViewItem.py')
    results = search_widgets / Path('Results.py')

    cabinet = widgets / Path('Cabinet.py')
    liquor_details = widgets / Path('LiquorDetails.py')
    liquor_view = widgets / Path('LiquorView.py')
    search = widgets / Path('Search.py')

    data_handler = cwd / Path('Data_Handler.py')
    main = cwd / Path('main.py')

    if not home.exists():
        return False
    elif not liquorviewitem.exists():
        return False
    elif not results.exists():
        return False
    elif not cabinet.exists():
        return False
    elif not liquor_details.exists():
        return False
    elif not liquor_view.exists():
        return False
    elif not search.exists():
        return False
    elif not data_handler.exists():
        return False
    elif not main.exists():
        return False
    else:
        return True


def main():
    """Main function which launches the widget
    """
    if check_filesystem():
        data_handler = Data_Handler()
        app = QApplication(sys.argv)
        instance = MainWindow(data_handler)
        instance.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()
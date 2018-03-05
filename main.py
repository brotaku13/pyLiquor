from PyQt5.QtWidgets import *

from Widgets.MainWindow import MainWindow
from Data_Handler import Data_Handler
import sys


def main():
    data_handler = Data_Handler()
    app = QApplication(sys.argv)
    instance = MainWindow(data_handler)
    instance.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
from PyQt5.QtWidgets import *

from Widgets.MainWindow import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    instance = MainWindow()
    instance.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
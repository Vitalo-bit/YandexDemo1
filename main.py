import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication



class YandexApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)
        self.setup_ui()

    def setup_ui(self):
        pass

def main(name):
    app = QtWidgets.QApplication(sys.argv)
    window = YandexApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main('PyCharm')

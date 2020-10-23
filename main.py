import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

class YandexApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()  # Это нужно для инициализации нашего дизайна
    def setup_ui(self):
        pass

def main(name):
    app = QtWidgets.QApplication(sys.argv)
    window = YandexApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')
# eg
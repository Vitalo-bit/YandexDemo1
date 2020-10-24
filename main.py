import sys
import csv
from PyQt5 import QtWidgets, uic, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QPushButton


class YandexApp(QtWidgets.QMainWindow):
    def __init__(self):
        self.my_csv_path = ""
        self.csv_reader = None
        self.csv_data = None
        self.csv_data_buttons = []
        self.chosenColumn = None
        super().__init__()
        uic.loadUi("design.ui", self)
        self.setup_ui()

    def setup_ui(self):
        self.trigger_stage_1()
        pass

    def trigger_stage_1(self):
        self.content_1.setVisible(True)
        self.content_2.setVisible(False)
        self.openFileBtn.clicked.connect(self.get_csv)
        self.openFileBtn.setStyleSheet("background: #c3fb12; font-size: 20px; padding: 9px; border-radius: 10px;")
        self.progressBar.setValue(0)
        self.csv_file_path.setText(self.my_csv_path)
        self.stage_1.setChecked(True)
        self.stage_1.setEnabled(True)
        self.stage_2.setChecked(False)
        self.stage_2.setEnabled(False)
        self.stage_3.setChecked(False)
        self.stage_3.setEnabled(False)
        self.stage_4.setChecked(False)
        self.stage_4.setEnabled(False)
        self.chooseDataRows.setStyleSheet("color: #000; border: 1px solid #000;")
        self.chooseDataRows.setEnabled(False)
        self.update()

    def trigger_stage_2(self):
        # self.content_1.hide()
        self.open_csv()
        self.content_1.setVisible(False)
        self.content_2.setVisible(True)
        self.progressBar.setValue(30)

    def get_csv(self):
        self.my_csv_path = QFileDialog.getOpenFileName(self, 'Выбрать файл с данными', '')[0]
        self.csv_file_path.setText(self.my_csv_path)
        self.chooseDataRows.setStyleSheet("background: #c3fb12; font-size: 20px; padding: 9px; border-radius: 10px; "
                                          "color: #000000;")
        self.chooseDataRows.setEnabled(True)
        self.openFileBtn.setStyleSheet("background: transparent; color: #c3fb12; border: 1px solid #c3fb12; "
                                       "font-size: 20px; padding: 9px; border-radius: 10px;")
        self.chooseDataRows.clicked.connect(self.trigger_stage_2)

    def open_csv(self):
        # csv_file = open(self.my_csv_path, "r")
        with open(self.my_csv_path, newline='') as f:
            self.csv_reader = csv.reader(f, delimiter=',')
            self.csv_data = list(self.csv_reader)
            # object =
            # self.vbox.addWidget(object)
        print(self.csv_data[0])
        data_layout = Qt.QVBoxLayout()
        self.csv_data_buttons.clear()
        column_id = 0
        for x in self.csv_data[0]:
            column_label = QPushButton(x)
            self.csv_data_buttons.append(column_label)
            column_label.clicked.connect(lambda: self.choose_data_row())
            data_layout.addWidget(column_label)
            column_id += 1

        w = Qt.QWidget()
        w.setLayout(data_layout)
        self.data_columns_area.setWidget(w)

    def choose_data_row(self):
        chosen_column_index = 0
        for x in self.csv_data_buttons:
            # print(x)
            x.setStyleSheet("background: #000;")
            if x == self.sender():
                self.chosenColumn = [x.text(), chosen_column_index]
                # print(self.chosenColumn)
            chosen_column_index += 1
        self.sender().setStyleSheet("background: #FFFFFF; color: #000;")
        self.chooseDataRepresentation.setStyleSheet("background: #c3fb12; font-size: 20px; padding: 9px; "
                                                    "border-radius: 10px; "
                                                    "color: #000000;")


def main(name):
    app = QtWidgets.QApplication(sys.argv)
    window = YandexApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main('YandexDemo1')

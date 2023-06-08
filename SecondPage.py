from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal
from FirstPage import FirstPage


class SecondPage(QWidget):
    sendData = pyqtSignal(str)

    def __init__(self, first_page):
        super().__init__()

        self.first_page = first_page

        self.label = QLabel("Data from First Page: None")
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.button = QPushButton("Send Data to First Page")
        self.button.clicked.connect(self.sendDataToFirstPage)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def sendDataToFirstPage(self):
        data = "Hello from Second Page"
        self.sendData.emit(data)

    def receiveData(self, data):
        self.label.setText("Data from First Page: " + str(data))


if __name__ == "__main__":
    app = QApplication([])
    first_page = FirstPage()
    second_page = SecondPage(first_page)

    first_page.sendData.connect(second_page.receiveData)
    second_page.sendData.connect(first_page.receiveData)

    first_page.show()
    second_page.show()
    app.exec_()

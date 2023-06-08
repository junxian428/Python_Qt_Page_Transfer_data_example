from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal


class FirstPage(QWidget):
    sendData = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.label = QLabel("Data from Second Page: None")
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.button = QPushButton("Send Data to Second Page")
        self.button.clicked.connect(self.sendDataToSecondPage)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def sendDataToSecondPage(self):
        data = "Hello from First Page"
        self.sendData.emit(data)

    def receiveData(self, data):
        self.label.setText("Data from Second Page: " + str(data))


if __name__ == "__main__":
    app = QApplication([])
    first_page = FirstPage()
    first_page.show()
    app.exec_()

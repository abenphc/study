import datetime

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
import sys


class ConnWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lcd = QLCDNumber()
        self.initUI()

        self.num = 0

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()
        self.button = QPushButton("start")
        self.button.clicked.connect(self.onClick)
        #        print("self1:",self)
        #       print(self.button)
        layout.addWidget(self.button)
        self.lcd.setDigitCount(5)
        self.lcd.display("00:00")
        layout.addWidget(self.lcd)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def onClick(self):
        #        print("self2:",self)
        sender = self.sender()
        #       print(sender)
        if sender.text() == "start":
            sender.setText("pause")
            self.timer = QTimer()
            self.timer.timeout.connect(self.display)
            self.timer.start(1000)
        else:
            sender.setText("start")
            self.timer.stop()

    def display(self):
        self.num += 1
        time_str = "{:02}:{:02}".format(self.num // 60, self.num % 60)
        self.lcd.display(time_str)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wid = ConnWidget()
    wid.setWindowTitle("第一个窗口程序")
    wid.show()
    sys.exit(app.exec())

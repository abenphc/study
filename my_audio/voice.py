# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voice.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import wave
from pyaudio import PyAudio, paInt16

channels = 1
sampwidth = 2
framerate = 8000
NUM_SAMPLES = 1024
TIME = 2


class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 260, 89, 25))
        self.pushButton.setText("开始录音")
        self.pushButton.clicked.connect(my_record)
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 260, 89, 25))
        self.pushButton_2.setText("结束录音")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 256, 192))


def save_wave_file(filename, data):
    '''save the data to the wav file'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    my_buf = []
    stream = pa.open(format=paInt16, channels=1,
                     rate=framerate, input=True,
                     input_device_index=-1,
                     frames_per_buffer=NUM_SAMPLES)
    count = 0
    while count < TIME * 20:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print(".")
    stream.stop_stream()
    stream.close()
    pa.terminate()
    save_wave_file('01.wav', my_buf)
    print('over')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec())

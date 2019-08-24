# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import requests
import json

dic = {"北京":"101010100","上海":"101020100","天津":"101030100"}

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 20, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 261, 131))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.queryWeather)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "北京"))
        self.comboBox.setItemText(1, _translate("Form", "上海"))
        self.comboBox.setItemText(2, _translate("Form", "天津"))
        self.pushButton.setText(_translate("Form", "查询"))

    def getcityCde(self,cityName):
        return dic[cityName]

    def queryWeather(self):
        cityName = self.comboBox.currentText()
        cityCode = self.getcityCde(cityName)
        req = requests.get('http://www.weather.com.cn/data/sk/'+cityCode + '.html')
        req.encoding = 'utf-8'
        data = req.json()
        print(data)

        msg1 = "城市:{}".format(data['weatherinfo']['city']+'\n')
        msg2 = "温度:{}".format(data['weatherinfo']['temp'] + '\n')
        msg3 = "风向:{}  风力:{}".format(data['weatherinfo']['WD'], data['weatherinfo']['WS']+ '\n')

        self.textEdit.append(msg1)
        self.textEdit.append(msg2)
        self.textEdit.append(msg3)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec())

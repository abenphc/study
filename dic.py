# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dic.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import QueryWord
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent



class Ui_Form(QWidget):
    def __init__(self):
        super().__init__()
        self.word = QueryWord.Word()
        self.player = QMediaPlayer()
        self.setupUi(self)
        self.setFocus()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMouseTracking(True)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 351, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setEnabled(False)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 230, 351, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 200, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 188, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fayin1 = QtWidgets.QLabel(self.widget)
        self.fayin1.setText("")
        self.fayin1.setObjectName("fayin1")
        self.horizontalLayout.addWidget(self.fayin1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.fayin2 = QtWidgets.QLabel(self.widget)
        self.fayin2.setText("")
        self.fayin2.setObjectName("fayin2")
        self.horizontalLayout.addWidget(self.fayin2)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.clipboard = QtGui.QGuiApplication.clipboard()
        self.clipboard.selectionChanged.connect(self.display)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", ""))

    def eventFilter(self, target, event):
        print("111")
        if target == self.fayin1 & event.type() == QtCore.QEvent.MouseMove:
            self.play_voice(self.word.voices[0][1])
        if target == self.fayin2 & event.type() == QtCore.QEvent.MouseMove:
            self.play_voice(self.word.voices[1][1])

    def play_voice(self,url):
        content = QMediaContent(QtCore.QUrl(url))
        self.player.setMedia(content)
        self.player.play()


    def focusOutEvent(self, a0: QtGui.QFocusEvent) -> None:
        self.hide()

    def display(self):
        text = self.clipboard.text(QtGui.QClipboard.Selection)
        if not text:
            return
        self.word = QueryWord.QueryWord().query(text)
        if not self.word.props:
            return
        print(self.word)
        if self.word.voices[0]:
            self.fayin1.setText(self.word.voices[0][0])
        if self.word.voices[1]:
            self.fayin2.setText(self.word.voices[1][0])
        str = ''
        for a, b in self.word.props.items():
            str += (a + " " + b + "\n")
        self.textEdit.setText(str)
        if self.word.label_text:
            self.label.setText(self.word.label_text)
        str = ''
        for a, b in self.word.changes.items():
            str += (a + b)
        self.textEdit_2.setText(str)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    ui = Ui_Form()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instragram.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(390, 490, 90, 28))
        self.start.setObjectName("start")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(40, 500, 90, 28))
        self.reset.setObjectName("reset")
        self.userid = QtWidgets.QLineEdit(self.centralwidget)
        self.userid.setGeometry(QtCore.QRect(190, 60, 301, 31))
        self.userid.setObjectName("userid")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(190, 120, 301, 31))
        self.password.setObjectName("password")
        self.hashtags = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.hashtags.setGeometry(QtCore.QRect(250, 180, 241, 181))
        self.hashtags.setObjectName("hashtags")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(360, 410, 121, 21))
        self.radioButton.setObjectName("radioButton")
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(30, 70, 58, 16))
        self.user.setObjectName("user")
        self.labelpass = QtWidgets.QLabel(self.centralwidget)
        self.labelpass.setGeometry(QtCore.QRect(30, 130, 81, 16))
        self.labelpass.setObjectName("labelpass")
        self.lab_hash = QtWidgets.QLabel(self.centralwidget)
        self.lab_hash.setGeometry(QtCore.QRect(30, 210, 91, 16))
        self.lab_hash.setObjectName("lab_hash")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 400, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_hash = QtWidgets.QLabel(self.centralwidget)
        self.label_hash.setGeometry(QtCore.QRect(30, 240, 201, 21))
        self.label_hash.setObjectName("label_hash")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 521, 61))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 0, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "Go"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.user.setText(_translate("MainWindow", "USER ID"))
        self.labelpass.setText(_translate("MainWindow", "PASSWORD"))
        self.lab_hash.setText(_translate("MainWindow", "HASHTAGS"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_hash.setText(_translate("MainWindow", "Atleast 10 different hashtags"))
        self.label_5.setText(_translate("MainWindow", "Instragram GUI Application"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

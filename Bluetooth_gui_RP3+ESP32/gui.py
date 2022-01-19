# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Display(object):
    def setupUi(self, Display):
        Display.setObjectName("Display")
        Display.resize(320, 320)
        Display.setMinimumSize(QtCore.QSize(320, 320))
        Display.setMaximumSize(QtCore.QSize(320, 320))
        self.centralwidget = QtWidgets.QWidget(Display)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("  background-color: rgb(0, 0, 0);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 3px;\n"
"  border-radius: 10px;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(170, 0, 0);\n"
"border: 2px solid #8f8f91;\n"
"border-radius: 20px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lcdNumber.setStyleSheet("  background-color: rgb(0, 0, 0);\n"
"  border: 2px solid rgb(113, 113, 113);\n"
"  border-width: 3px;\n"
"  border-radius: 5px;\n"
"  color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 100000.0)
        self.lcdNumber.setProperty("intValue", 100000)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_2.addWidget(self.lcdNumber, 1, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
" QProgressBar::chunk {\n"
"     background-color: #3add36;\n"
"     width: 18px;\n"
"     margin: 2px;   \n"
" }\n"
"")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)
        Display.setCentralWidget(self.centralwidget)

        self.retranslateUi(Display)
        QtCore.QMetaObject.connectSlotsByName(Display)

    def retranslateUi(self, Display):
        _translate = QtCore.QCoreApplication.translate
        Display.setWindowTitle(_translate("Display", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Display = QtWidgets.QMainWindow()
    ui = Ui_Display()
    ui.setupUi(Display)
    Display.show()
    sys.exit(app.exec_())

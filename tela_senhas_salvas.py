# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_senhas_salvas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_senhas_salvas(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 506)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_voltar.setGeometry(QtCore.QRect(600, 50, 91, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setStyleSheet("QPushButton{ background: #0BAEE1;border-radius: 10px;}QPushButton:hover{color: white;}")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.labe_adc_senha = QtWidgets.QLabel(self.centralwidget)
        self.labe_adc_senha.setGeometry(QtCore.QRect(270, 100, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labe_adc_senha.setFont(font)
        self.labe_adc_senha.setObjectName("labe_adc_senha")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(40, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Logo.setObjectName("Logo")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 150, 531, 321))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.labe_adc_senha.setText(_translate("MainWindow", "senhas salvas"))
        self.Logo.setText(_translate("MainWindow", "PassKey"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_senhas_salvas()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
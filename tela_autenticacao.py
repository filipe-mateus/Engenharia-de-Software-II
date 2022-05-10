# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_autenticacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 681)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEntrar.setGeometry(QtCore.QRect(280, 360, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.botaoEntrar.setFont(font)
        self.botaoEntrar.setStyleSheet("background: #0BAEE1;\n"
"border-radius: 10px;")
        self.botaoEntrar.setObjectName("botaoEntrar")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Logo.setObjectName("Logo")
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setGeometry(QtCore.QRect(210, 290, 261, 41))
        self.lineEdit_codigo.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);")
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.label_msg = QtWidgets.QLabel(self.centralwidget)
        self.label_msg.setGeometry(QtCore.QRect(100, 230, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName("label_msg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 21))
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
        self.botaoEntrar.setText(_translate("MainWindow", "Entrar"))
        self.Logo.setText(_translate("MainWindow", "PassKay"))
        self.label_msg.setText(_translate("MainWindow", "Insira o código enviado no seu e-mail:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
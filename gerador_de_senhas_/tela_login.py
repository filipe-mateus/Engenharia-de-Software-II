# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botaoEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.botaoEntrar.setGeometry(QtCore.QRect(260, 340, 131, 41))
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
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(200, 230, 261, 31))
        self.lineEdit_usuario.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);")
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setGeometry(QtCore.QRect(200, 290, 261, 31))
        self.lineEdit_senha.setStyleSheet("border-radius: 10px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: rgb(156, 156, 156);")
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.label_usuario = QtWidgets.QLabel(self.centralwidget)
        self.label_usuario.setGeometry(QtCore.QRect(100, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_usuario.setFont(font)
        self.label_usuario.setObjectName("label_usuario")
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setGeometry(QtCore.QRect(110, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_senha.setFont(font)
        self.label_senha.setObjectName("label_senha")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(290, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 21))
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
        self.label_usuario.setText(_translate("MainWindow", "Usuario:"))
        self.label_senha.setText(_translate("MainWindow", "Senha:"))
        self.label_login.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tela_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_menu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(20, 20, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Logo.setFont(font)
        self.Logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Logo.setObjectName("Logo")
        self.label_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(280, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_menu.setFont(font)
        self.label_menu.setObjectName("label_menu")
        self.pushButton_salvar_senha = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar_senha.setGeometry(QtCore.QRect(210, 220, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_salvar_senha.setFont(font)
        self.pushButton_salvar_senha.setStyleSheet("QPushButton{ background: #0BAEE1;border-radius: 10px;}QPushButton:hover{color: white;}")
        self.pushButton_salvar_senha.setObjectName("pushButton_salvar_senha")
        self.pushButton_gerar_senha = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gerar_senha.setGeometry(QtCore.QRect(210, 270, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_gerar_senha.setFont(font)
        self.pushButton_gerar_senha.setStyleSheet("QPushButton{ background: #0BAEE1;border-radius: 10px;}QPushButton:hover{color: white;}")
        self.pushButton_gerar_senha.setObjectName("pushButton_gerar_senha")
        self.pushButton_sair = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair.setGeometry(QtCore.QRect(210, 370, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sair.setFont(font)
        self.pushButton_sair.setStyleSheet("QPushButton{ background: #0BAEE1;border-radius: 10px;}QPushButton:hover{color: white;}")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.pushButton_sair_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sair_2.setGeometry(QtCore.QRect(210, 320, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sair_2.setFont(font)
        self.pushButton_sair_2.setStyleSheet("QPushButton{ background: #0BAEE1;border-radius: 10px;}QPushButton:hover{color: white;}")
        self.pushButton_sair_2.setObjectName("pushButton_sair_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 21))
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
        self.Logo.setText(_translate("MainWindow", "PassKey"))
        self.label_menu.setText(_translate("MainWindow", "Menu"))
        self.pushButton_salvar_senha.setText(_translate("MainWindow", "Salvar senha"))
        self.pushButton_gerar_senha.setText(_translate("MainWindow", "Gerar senha"))
        self.pushButton_sair.setText(_translate("MainWindow", "Sair"))
        self.pushButton_sair_2.setText(_translate("MainWindow", "ver senhas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_menu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

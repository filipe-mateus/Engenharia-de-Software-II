import random
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication


from tela_adicionar_senha import Tela_adicionar_senha
from tela_autenticacao import Tela_autentica
from tela_criar_conta import Tela_criar_conta
from tela_gerar_senha import Tela_gerar_senha
from tela_login import Tela_login
from tela_menu import Tela_menu


#from ...src.usuario import *

from src.usuario import as_init
from src.cadastro import *



class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()


        self.login = Tela_login()
        self.login.setupUi(self.stack0)

        self.criar_conta = Tela_criar_conta()
        self.criar_conta.setupUi(self.stack1)

        self.gerar_senha = Tela_gerar_senha()
        self.gerar_senha.setupUi(self.stack2)

        self.autentica = Tela_autentica()
        self.autentica.setupUi(self.stack3)

        self.adicionar_senha = Tela_adicionar_senha()
        self.adicionar_senha.setupUi(self.stack4)

        self.menu = Tela_menu()
        self.menu.setupUi(self.stack5)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)

class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        
        
        self.login.botaoEntrar_cadastresse.clicked.connect(self.abrir_tela_criar_conta)
        self.login.botaoEntrar.clicked.connect(self.abrir_tela_gerar_senha)

        self.criar_conta.botao_criar.clicked.connect(self.botao_criar)
        #self.busca.pushButton_5.clicked.connect(self.botaoBusca)
        self.criar_conta.botao_voltar.clicked.connect(self.botaoVoltar)
        self.gerar_senha.pushButton_copiar_2.clicked.connect(self.abrir_tela_adiciona_senha)

    botaoVoltar = lambda self: self.QtStack.setCurrentIndex(0)

    def email_existe(self, usuario):
        for i in self.usuarios:
            if(i.email == usuario.email):
                return True
            
    
    def botao_criar(self):
        email = self.criar_conta.lineEdit_email.text()
        senha = self.criar_conta.lineEdit_senha.text()
        confirmar_senha = self.criar_conta.lineEdit_confirmarSenha.text()
        
        if not (email == '' or senha == '' or confirmar_senha == ''):
            if (senha == confirmar_senha):

                if (self.email_existe):
                    usuario = Usuario(email, senha)
                    self.usuarios.append(usuario)
                    QMessageBox.information(None, 'Passkey', 'Cadastro realizado com sucesso!')
                    self.criar_conta.lineEdit_email.setText('')
                    self.criar_conta.lineEdit_senha.setText('')
                    self.criar_conta.lineEdit_confirmarSenha.setText('')
                    flag = 0
                else:
                    QMessageBox.information(None, 'Passkey', 'O email informado ja está cadastrado!')
                    flag = 1
            else:
                QMessageBox.information(None, 'Passkey', 'As senhas não são iguais, tente novamente!')
                flag = 1
        else:
            QMessageBox.information(None, 'Passkey', 'Todos os valores devem ser preenchidos!')
            flag = 1

        if (flag == 1):
            self.QtStack.setCurrentIndex(1)
        else:
            self.QtStack.setCurrentIndex(0)


    def botaoBusca(self):
        cpf = self.busca.lineEdit_5.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.busca.lineEdit_6.setText(pessoa.nome)
            self.busca.lineEdit_7.setText(pessoa.endereco)
            self.busca.lineEdit_8.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, 'POOII', 'CPF NAO ENCONTRADO!')

    def abrir_tela_criar_conta(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_gerar_senha(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_adiciona_senha(self):
        self.QtStack.setCurrentIndex(4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
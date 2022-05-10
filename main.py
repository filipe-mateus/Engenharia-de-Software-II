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


        self.Tela = Tela_login()
        self.Tela.setupUi(self.stack0)

        self.cadastro = Tela_criar_conta()
        self.cadastro.setupUi(self.stack1)

        self.busca = Tela_gerar_senha()
        self.busca.setupUi(self.stack2)

        self.busca = Tela_autentica()
        self.busca.setupUi(self.stack3)

        self.busca = Tela_adicionar_senha()
        self.busca.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)

class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        
        self.Tela.botaoEntrar_cadastresse.clicked.connect(self.abrir_tela_criar_conta)
        #self.Tela.pushButton_2.clicked.connect(self.abrirTelaBusca)

        #self.cadastro.pushButton_6.clicked.connect(self.botaoCadastra)
        #self.busca.pushButton_5.clicked.connect(self.botaoBusca)
        #self.busca.pushButton_voltar.clicked.connect(self.botaoVoltar)

    #botaoVoltar = lambda self: self.QtStack.setCurrentIndex(0)
    '''
    def botaoCadastra(self):
        nome = self.cadastro.lineEdit.text()
        endereco = self.cadastro.lineEdit_2.text()
        cpf = self.cadastro.lineEdit_3.text()
        nascimento = self.cadastro.lineEdit_4.text()
        if not (nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            p = Pessoa(nome,endereco,cpf,nascimento)
            if (self.cad.cadastra(p)):
                QMessageBox.information(None, 'POOII', 'Cadastro realizado com sucesso!')
                self.cadastro.lineEdit.setText('')
                self.cadastro.lineEdit_2.setText('')
                self.cadastro.lineEdit_3.setText('')
                self.cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POOII', 'O cpf informado ja está cadastrado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos!')

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

'''
    def abrir_tela_criar_conta(self):
        self.QtStack.setCurrentIndex(1)
'''
    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(2)


    def gerar_senha(caracteres, minusculas, maiusculas, numeros, especial):
    minus = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
             "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "v"]
    maius = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
             "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "V"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    esp = ["!", "@", "#", "$", "%", "^", "&", "*"]
    construtora = []
    if minusculas:
        construtora.append(minus)
    if maiusculas:
        construtora.append(maius)
    if numeros:
        construtora.append(num)
    if especial:
        construtora.append(esp)
    senha = ""
    for i in range(0, caracteres):
        aux = random.choice(construtora)
        senha = senha + random.choice(aux)

    print("Senha: {}".format(senha))

    #gerar_senha(12, True, True, True, False)

    '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
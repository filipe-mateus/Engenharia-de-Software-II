from mimetypes import init
import random
import sys
import os
import pyperclip

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication


from tela_adicionar_senha import Tela_adicionar_senha
from tela_autenticacao import Tela_autentica
from tela_criar_conta import Tela_criar_conta
from tela_gerar_senha import Tela_gerar_senha
from tela_login import Tela_login
from tela_menu import Tela_menu
from tela_senhas_salvas import Tela_senhas_salvas


from src.usuario import *
from src.cadastro import *
from src.enviar_email import *




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
        self.stack6 = QtWidgets.QMainWindow()


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

        self.senhas_salvas = Tela_senhas_salvas()
        self.senhas_salvas.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):

    

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.dic_usuario = {}
        self.cad = Cadastro()
        
        
        
        self.login.botaoEntrar_cadastresse.clicked.connect(self.abrir_tela_criar_conta)
        #self.login.botaoEntrar.clicked.connect(self.abrir_tela_gerar_senha)

        self.criar_conta.botao_criar.clicked.connect(self.botao_criar)
        #self.busca.pushButton_5.clicked.connect(self.botaoBusca)

        self.menu.pushButton_gerar_senha.clicked.connect(self.abrir_tela_gerar_senha)
        self.menu.pushButton_salvar_senha.clicked.connect(self.abrir_tela_adiciona_senha)
        self.menu.pushButton_sair_2.clicked.connect(self.abrir_tela_ver_senhas)

        self.login.botaoEntrar.clicked.connect(self.botao_entrar)
        self.autentica.botaoEntrar.clicked.connect(self.botao_entrar_autentica)
        self.autentica.botaoEntrar_3.clicked.connect(self.botao_enviar_autentica)
        self.gerar_senha.pushButton_gera.clicked.connect(self.botao_gerar_senha)
        self.gerar_senha.pushButton_copiar.clicked.connect(self.botao_copiar)
        self.gerar_senha.pushButton_copiar.clicked.connect(self.botao_copiar)
        self.gerar_senha.pushButton_salvar_senha.clicked.connect(self.botao_salvar_senha)
        
        self.adicionar_senha.pushButton_salva.clicked.connect(self.botao_salvar_adiciona)
        self.adicionar_senha.pushButton_cancelar.clicked.connect(self.botao_cancelar_adiciona)
        
        
        
        self.criar_conta.botao_voltar.clicked.connect(self.botaoVoltar)
        self.autentica.botaoEntrar_2.clicked.connect(self.botaoVoltar)
        self.menu.pushButton_sair.clicked.connect(self.botaoVoltar)
        self.gerar_senha.pushButton_volta.clicked.connect(self.botaoVoltar_menu)
        self.adicionar_senha.pushButton_voltar.clicked.connect(self.botaoVoltar_menu)
        self.senhas_salvas.pushButton_voltar.clicked.connect(self.botaoVoltar_menu)
        

    botaoVoltar = lambda self: self.QtStack.setCurrentIndex(0)
    botaoVoltar_menu = lambda self: self.QtStack.setCurrentIndex(5)
      
    def botao_criar(self):
        email = self.criar_conta.lineEdit_email.text()
        senha = self.criar_conta.lineEdit_senha.text()
        codigo = 0
        confirmar_senha = self.criar_conta.lineEdit_confirmarSenha.text()
        
        if not (email == '' or senha == '' or confirmar_senha == ''):
            if (senha == confirmar_senha):
                usuario = Usuario(email,senha,codigo)
                if (self.cad.cadastra(usuario)):
                    self.dic_usuario[email] = Usuario(email,senha,codigo)
                    QMessageBox.information(None, 'Passkey', 'Cadastro realizado com sucesso!')
                    self.criar_conta.lineEdit_email.setText('')
                    self.criar_conta.lineEdit_senha.setText('')
                    self.criar_conta.lineEdit_confirmarSenha.setText('')
                    flag = 0
                else:
                    QMessageBox.information(None, 'Passkey', 'O email informado ja está cadastrado!')
                    self.criar_conta.lineEdit_email.setText('')
                    self.criar_conta.lineEdit_senha.setText('')
                    self.criar_conta.lineEdit_confirmarSenha.setText('')
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

    def botao_entrar(self):
        email = self.login.lineEdit_usuario.text()
        senha = self.login.lineEdit_senha.text()

        if not (email == '' or senha == ''):
            if(self.cad.busca(email) != None):
                if(senha in self.dic_usuario[email].senha):
                    self.login.lineEdit_senha.setText('')
                    flag = 0
                else:
                    QMessageBox.information(None, 'Passkey', 'Senha incorreta!')
                    self.login.lineEdit_senha.setText('')
                    flag = 1 
            else:
                QMessageBox.information(None, 'Passkey', 'O email informado não está cadastrado!')
                self.login.lineEdit_usuario.setText('')
                self.login.lineEdit_senha.setText('')
                flag = 1
        else:
            QMessageBox.information(None, 'Passkey', 'Todos os valores devem ser preenchidos!')
            flag = 1

        if (flag == 1):
            self.QtStack.setCurrentIndex(0)
            return None
        else:
            self.QtStack.setCurrentIndex(3)

    

    def botao_enviar_autentica(self):
        pass
        '''
        email = self.login.lineEdit_usuario.text()
        send = Codigo_verific(email)
        codigo = send.enviar_email()
        codigo = int(codigo)
        self.dic_usuario[email].codigo = codigo
        QMessageBox.information(None, 'Passkey', 'Código enviado!')
        '''

    def botao_entrar_autentica(self):
        '''
        email = self.login.lineEdit_usuario.text()
        codigo_digitado = self.autentica.lineEdit_codigo.text()
        codigo_digitado = int(codigo_digitado)
        if(self.dic_usuario[email].codigo == codigo_digitado):
            self.QtStack.setCurrentIndex(5)
        else:
            QMessageBox.information(None, 'Passkey', 'Código diferente!')
        '''
        if(1 == 1):
            self.QtStack.setCurrentIndex(5)

   
    
    def botao_gerar_senha(self):

        num_senha = self.gerar_senha.lineEdit_num_senha.text()
        num_senha = int(num_senha)
        maiuscula = 0
        minuscula = 0
        numero = 0
        caracter_especial = 0

        if(self.gerar_senha.checkBox_letra_maiuscula.isChecked()):
            maiuscula = 1
        if(self.gerar_senha.checkBox_letra_minuscula.isChecked()):
            minuscula = 1
        if(self.gerar_senha.checkBox_numero.isChecked()):
            numero = 1
        if(self.gerar_senha.checkBox_carac_especial.isChecked()):
            caracter_especial  = 1
        
        senha_gerada = self.cad.gerar_senha(num_senha,minuscula,maiuscula,numero,caracter_especial)
        self.gerar_senha.lineEdit_senha.setText(senha_gerada)

    def botao_copiar(self):
        senha = self.gerar_senha.lineEdit_senha.text()
        pyperclip.copy(senha)
    
    def botao_salvar_adiciona(self):
        email = self.login.lineEdit_usuario.text()
        url = self.adicionar_senha.lineEdit_url.text()
        nome_usuario = self.adicionar_senha.lineEdit_nam_usuari.text()
        senha_site = self.adicionar_senha.lineEdit_pswd_sit.text()
        categoria = self.adicionar_senha.lineEdit_categori.text()

        self.dic_usuario[email].dic_senhas_salvas[url] = Dados_senha(url,nome_usuario,senha_site,categoria)

        

        string_senhas = ''

        for i in self.dic_usuario[email].dic_senhas_salvas:
            url = (self.dic_usuario[email].dic_senhas_salvas[i].url)
            nome_usuario = (self.dic_usuario[email].dic_senhas_salvas[i].nome_usuario)
            senha_site = (self.dic_usuario[email].dic_senhas_salvas[i].senha_site)
            categoria = (self.dic_usuario[email].dic_senhas_salvas[i].categoria)
            string_senhas += f"url: {url}\nnome do usuário: {nome_usuario}\nsenha do site: {senha_site}\ncategoria: {categoria}\n\n" 


        self.senhas_salvas.textEdit.setText(string_senhas)

        self.adicionar_senha.lineEdit_url.setText('')
        self.adicionar_senha.lineEdit_nam_usuari.setText('')
        self.adicionar_senha.lineEdit_pswd_sit.setText('')
        self.adicionar_senha.lineEdit_categori.setText('')


        self.QtStack.setCurrentIndex(6)

    def botao_cancelar_adiciona(self):
        self.adicionar_senha.lineEdit_url.setText('')
        self.adicionar_senha.lineEdit_nam_usuari.setText('')
        self.adicionar_senha.lineEdit_pswd_sit.setText('')
        self.adicionar_senha.lineEdit_categori.setText('')
        self.QtStack.setCurrentIndex(5)


    def botao_salvar_senha(self):

        senha_gerada = self.gerar_senha.lineEdit_senha.text()
        self.gerar_senha.checkBox_letra_maiuscula.setChecked(False)
        self.gerar_senha.checkBox_letra_minuscula.setChecked(False)
        self.gerar_senha.checkBox_numero.setChecked(False)
        self.gerar_senha.checkBox_carac_especial.setChecked(False)
        self.gerar_senha.lineEdit_num_senha.setText('')
        self.QtStack.setCurrentIndex(4)
        self.adicionar_senha.lineEdit_pswd_sit.setText(senha_gerada)

    def abrir_tela_menu(self):
        self.QtStack.setCurrentIndex(5)

    def abrir_tela_criar_conta(self):
        self.QtStack.setCurrentIndex(1)

    def abrir_tela_gerar_senha(self):
        self.QtStack.setCurrentIndex(2)

    def abrir_tela_adiciona_senha(self):
        self.QtStack.setCurrentIndex(4)

    def abrir_tela_ver_senhas(self):
        self.QtStack.setCurrentIndex(6)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
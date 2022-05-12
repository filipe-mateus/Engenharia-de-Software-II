import random
from src.usuario import *

class Cadastro:

    
    def __init__(self):
        self.dic_usuario = {}

    def cadastra(self, usuario):
        existe =  self.busca(usuario.email)
        if(existe == None):
            self.dic_usuario[usuario.email] = usuario
            return  True
        else:
            return False

    def busca(self, email):
        if email in self.dic_usuario:
            return  email
        return None

    def gerar_senha(self, caracteres, minusculas, maiusculas, numeros, especial):
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

        return senha
        


class Usuario:


    def __init__(self, email, senha, codigo):
        self.email = email
        self.senha = senha
        self.codigo = codigo
        self.dic_senhas_salvas = {}
    
class Dados_senha:

    def __init__(self, url, nome_usuario, senha_site, categoria):
        self.url = url
        self.nome_usuario = nome_usuario
        self.senha_site = senha_site
        self.categoria = categoria

        

        
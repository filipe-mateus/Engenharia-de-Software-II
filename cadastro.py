class Cadastro:


    def __init__(self):
        self._lista_email = []

    def cadastra(self, pessoa):
        existe =  self.busca(pessoa.cpf)
        if(existe == None):
            self._lista_pessoas.append(pessoa)
            return  True
        else:
            return False

    def busca(self, email):
        for i in self._lista_email:
            if i.email == email:
                return  i
        return None
class Cadastro:

    
    def __init__(self):
        self._lista_emails = []

    def cadastra(self, usuario):
        existe =  self.busca(usuario.email)
        if(existe == None):
            self._lista_emails.append(usuario)
            return  True
        else:
            return False

    def busca(self, email):
        for i in self._lista_emails:
            if i.email == email:
                return  i
        return None
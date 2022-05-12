
class Historico:

    def __init__(self):
        self.senhas = []

    def imprime(self, res):
        for i in self.senhas:
            res.append(i)
        return "\n".join(res)
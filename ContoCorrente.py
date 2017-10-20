class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto


class ContoCorrente(Conto):

    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.saldo)
        self.deposita(importo)

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.saldo)


class GestoreContiCorrenti:

    @staticmethod
    def bonifico(contoSrc, contoDst, importo):
        contoSrc.preleva(importo)
        contoDst.deposita(importo)


c1 = ContoCorrente("Matteo", "10", 2000)
c2 = ContoCorrente("Francesca", "20", 3000)

c1.descrizione()
c2.descrizione()

c1.deposita(500)
c1.descrizione()

c2.preleva(200)
c2.descrizione()

c1.saldo = 10000
c1.descrizione()

GestoreContiCorrenti.bonifico(c1, c2, 10)
c1.descrizione()
c2.descrizione()
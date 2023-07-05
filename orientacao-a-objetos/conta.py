

class Conta:

    def __init__(self, numero, titular, saldo, limite, codigo_banco):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = codigo_banco = "001"

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        limite_de_saldo = self.__saldo + self.__limite
        return valor_a_sacar <= limite_de_saldo

    def saca(self, valor):
        # if (valor <= (self.__saldo + self.__limite)):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))

    def transfere(self, valor, origem, destino):
        # origem.saca(valor)
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saLdo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        # return __codigo_banco
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
    
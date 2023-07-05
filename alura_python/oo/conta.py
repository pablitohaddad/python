class Conta: 

    def __init__(self, numero, titular, saldo, limite):
        print(f"Você digitou algo ... // {self}")

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print (f"Saldo do titular {self.__titular}: R${self.__saldo}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor R${valor} passou o limite ")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def transfere(self, valor, destino):
        self.saca(valor) 
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular.title()
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

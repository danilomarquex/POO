class Conta(object):
    def __init__(self, id_conta,id_cliente,saldo):
        self.id_conta = id_conta
        self.id_cliente = id_cliente  
        self.saldo = saldo
    def __str__(self):
        return " Conta: {} \n Cliente: {} \n Saldo: {}" .format(self.id_conta, self.id_cliente, self.saldo)
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta):
        if valor <= self.saldo:
            self.sacar(valor)
            conta.depositar(valor)
            return True
        else:
            return False


# testando código
contatest = Conta(245334, "Elane", 2500)
contatest.sacar(500)
contatest.depositar(20)

contatest2 = Conta(4535, "João", 500)
contatest2.transferir(50, contatest)
print(contatest)

print(contatest2)

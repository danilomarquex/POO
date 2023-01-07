class Conta:
    def __init__(self, cli, num, saldo = 0):
        self.cli = cli
        self.num = num
        self.saldo = saldo

    def __str__(self):
        return ' Cliente: {} \n Numero: {} \n Saldo: {}' .format(self.cli, self.num, self.saldo)

# definir os metodos saque, deposito e transferir 

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else: 
            print('Saque incompleto')
    
    def deposito(self, valor):
        if self.saldo >= valor:
            self.saldo += valor
        else:
            print('Deposito incompleto')
    
    def transferir(self, valor, conta):
        if self.saldo >= valor:
            conta.deposito = valor
        else: 
            print('acao incompleta')
class Conta:
    def __init__(self,clientes,numero,saldo = 0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
    def __str__(self):
        return " Número: {} \n Saldo: {}" .format(self.numero, self.saldo)
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque",valor])
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["Deposito",valor])

class Conta_Especial(Conta):
    def __init__(self, clientes, numero, saldo, limite, debito = 0):
        super().__init__(clientes, numero, saldo)
        self.clientes = clientes 
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
        self.limite = limite 
        self.debito = debito

    def extrato(self):
        print("Numero C.: {}".format(self.numero))
        for op in self.operacoes:
            print('%10s %10.2f' % (op[0],op[1])) 
        print('%10s %10.2f\n' % ('Saldo =' ,self.saldo))
        print('Limite: {}\nDebito: {}' .format(self.limite, self.debito))

    def depositar(self, valor):
        if self.debito > 0:
            if  valor <= 0:
                self.debito -= valor
                self.limite += valor
                self.operacoes.append(["Deposito",valor])
            else:
                d = valor - self.debito
                self.saldo += d
                self.operacoes.append(["Deposito",valor])
                self.limite += self.debito 
                self.debito = 0
        else:
            self.saldo += valor
            self.operacoes.append(["Deposito",valor])

    def saque(self, valor):
        if valor <= (self.saldo+self.limite):
            self.saldo -= valor
            self.operacoes.append(["Saque",valor])
            if self.saldo < 0:
                self.debito -= (self.saldo)
                self.limite += self.saldo
                self.saldo = 0
                return True
            return True
        else:
            return False
                                                                    
    def transferir(self, valor, conta):
        if self.saque(valor):
           conta.depositar(valor)
           #self.operacoes.append(["Transferência",valor])
           return True
        else:
            return False

    def __str__(self):
        return super().__str__() + " \n Limite: {} \n Debito: {}" .format(self.limite, self.debito)

# Execução/instâncias
contatest01 = Conta_Especial('Danilo', 45234, 350, 1000, 640)
contatest02 = Conta_Especial('Ana', 53453, 200, 650, 200)

contatest01.saque(20)
contatest02.transferir(100, contatest01)
contatest02.saque(50)

print('<<operações conta 01>>')
print(contatest01.operacoes)
print(contatest01)

print('<<operações conta 02>>')
print(contatest02.operacoes)
print(contatest02)
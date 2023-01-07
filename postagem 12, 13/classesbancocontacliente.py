class Banco:
    def __init__(self, nome):
        self.__nome = nome
        self.__contas = []
    
    @property
    def nome(self):
        return self.__nome
    @property
    def contas(self):
        return self.__contas
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    @contas.setter
    def contas(self, valor):
        self.__contas = valor

    # métodos
    def adicionar(self, valor):
        self.__contas.append(valor)
    
    def remover(self, valor):
        if self.pesquisar(valor) != None:
            self.__contas.remove(self.pesquisar(valor))
    
    #pesquisa o nome de alguma pessoa dentro da lista de contas
    def pesquisar(self, valor):
        for i in range(len(self.__contas-1)):
            if self.__contatos[i] == valor:
                return self.__contatos[i]
        return None
    
    def valorTotal(self):
        v = 0
        for i in range(len(self.__contas)):
            v += self.__contas[i].saldo
        return v

    def __str__(self):
        return "{}\ncontas: {}\nvalor total: {}\n".format(self.__nome, self.__contas, self.valorTotal())

class Conta:
    def __init__(self, titular, numero, saldo=0):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def numero(self):
        return self.__numero
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,valor):
        self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("o saque é maior que o saldo\n")

    def __str__(self):
        return "{}\nnumero: {}\nsaldo: {}\n".format(self.__titular,self.__numero,self.__saldo)

    def __repr__(self):
        return "{}\nnumero: {}\nsaldo: {}\n".format(self.__titular,self.__numero,self.__saldo)

class Cliente:
    def __init__(self,cpf,nome):
        self.__cpf = cpf
        self.__nome = nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return "{}\ncpf: {}\n".format(self.__nome,self.__cpf)



# #testes
# #   bancos
# itau= Banco("Itau")
# bb= Banco("Banco do Brasil")
# santander= Banco("Santander")

# #   conta
# ca = Conta("João",123,3)
# cb = Conta("Augusto",234,432)
# cc = Conta("Manoel",345,32)
# cd = Conta("Ana",654,543)
# ce = Conta("Maria",546,123)
# cf = Conta("Joana",645,1000)

# #   Cliente
# joao= Cliente(123456,"João")
# ana= Cliente(654321,"Ana")
# Maria= Cliente(543216,"Maria")

# #   testes
# itau.adicionar(ca)
# itau.adicionar(cb)
# bb.adicionar(cc)
# bb.adicionar(cd)
# santander.adicionar(ce)
# santander.adicionar(cf)

# ca.sacar(4)
# cb.depositar(40)

# cc.depositar(32)
# cd.sacar(234)

# ce.sacar(102)
# cf.depositar(324)
# print(itau)
# print(bb)
# print(santander)
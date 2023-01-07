class Conta:
    def __init__(self,numero,cli,saldo=0):
        self.numero=numero
        self.cli=cli
        self.saldo=saldo
        self.operacoes=[]

    def deposito(self,valor):
        self.saldo+=valor

    def saque(self,valor):
        if valor<=self.saldo:
            self.saldo-=valor        
            return True        
        return False

    def transfere(self,valor,conta):
        if self.saque(valor):
           conta.deposito(valor)
           return True
        return False

class ContaEspecial(Conta):
    def __init__(self,numero,cli,saldo=0,limite=0):
        super().__init__(numero,cli,saldo)
        self.limite=limite
        self.__lt=limite

    def saque(self,valor):
        if (self.saldo+self.limite)>=valor:
            op=self.saldo-valor
            if op>=0:
                self.saldo=op                  
            else:
                pass
                
            return True
        return False

    def deposito(self,valor):
        if self.limite==self.__lt:
            super().deposito(valor)
        else:              
            pass

class Conta:
    def _init_(self,clientes,numero,saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
    

    def _str_(self):
          return "Número:{}\nSaldo:{}".format(self.numero,self.saldo)
    
    def saque(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            self.operacoes.append(["Saque",valor])
    
    def deposito(self,valor):
        self.saldo+=valor
        self.operacoes.append(["Deposito",valor])
    

class ContaEspecial(Conta):
     def _init_(self,clientes,numero,saldo=0,limite=0):
         super()._init_(clientes,numero,saldo)
         self.clientes = clientes 
         self.numero = numero
         self.saldo = saldo
         self.operacoes = []
         self.limite = limite 
     
     def depositar(self,valor):
              if  valor<=0:
                    self.limite+=valor
                    self.operacoes.append(["Deposito",valor])
                    print("deposito efetuado")
              else:
                    return False

     def saque(self,valor):
        if valor<=(self.saldo+self.limite):
           self.saldo-=valor
           self.operacoes.append(["Saque",valor])
           return True
        else:
            return False
          
                                                                            
     def transferir(self,valor,conta):
       if self.saque(valor):
           conta.depositar(valor)
           self.operacoes.append(["Transferência",valor])
           return True
       else:
         return False

     def _str_(self):
        return super()._str_()+"\n"+"Limite:{}".format(self.limite,self.debito)

E=Conta("Talia",24,243)
D=Conta("Eloisa",3,650)   
B=ContaEspecial("Tulio",1,850,600)
A=ContaEspecial("Caio",2,0,800)
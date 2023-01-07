class Conta:
    def __init__(self,clientes,numero,saldo=0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.operacoes = []
    

    def __str__(self):
          return "Número:{}\nSaldo:{}".format(self.numero,self.saldo)
    
    def saque(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            self.operacoes.append(["Saque",valor])
    
    def deposito(self,valor):
        self.saldo+=valor
        self.operacoes.append(["Deposito",valor])
    

class Conta_Especial(Conta):
     def __init__(self,clientes,numero,saldo,limite,debito=0):
         super().__init__(clientes,numero,saldo)
         self.clientes = clientes 
         self.numero = numero
         self.saldo = saldo
         self.operacoes = []
         self.limite = limite 
         self.debito = debito


     def extrato(self):
         print("Numero C.:{}".format(self.numero))
         for op in self.operacoes:
             print('%10s %10.2f' % (op[0],op[1])) 
         print('%10s %10.2f\n' % ('Saldo=',self.saldo))
         print("Limite:{}".format(self.limite))
         print("Debito:{}".format(self.debito))
     
     def depositar(self,valor):
            if self.debito>0:
                if  valor<=0:
                    self.debito-=valor
                    self.limite+=valor
                    self.operacoes.append(["Deposito",valor])
                else:
                    d=valor-self.debito
                    self.saldo+=d
                    self.operacoes.append(["Deposito",valor])
                    self.limite+=self.debito 
                    
                    self.debito=0
            else:
                self.saldo+=valor
                self.operacoes.append(["Deposito",valor])


     def saque(self,valor):
        if valor<=(self.saldo+self.limite):
           self.saldo-=valor
           self.operacoes.append(["Saque",valor])
           if self.saldo<0:
               self.debito=-(self.saldo)
               self.limite+=self.saldo
               
               self.saldo=0
               return True
           return True
        else:
            return False
          
                                                                            
     def transferir(self,valor,conta):
       if self.saque(valor):
           conta.depositar(valor)
           #self.operacoes.append(["Transferência",valor])
           return True
       else:
         return False

     def __str__(self):
        return super().__str__()+"\n"+"Limite:{}\nDebito:{}".format(self.limite,self.debito)
    
    
c1=Conta_Especial("Ray",1,850,600)
c2=Conta_Especial("Rian",2,0,800)


'''#c1.depositar(150)
#c1.saque(100)
c1.transferir(100,c2)
c1.extrato()
print("="*40)

c2.extrato()   ''' 

from tkinter import *


dicio={'cliente':'','numero':00,'saldo':00,'limite':00,'debito':00}
def criar():
    c=cliente.get()
    n=numero.get()
    s=saldo.get()
    l=limite.get()
    d=debito.get()
    obj1=Conta_Especial(c,int(n),int(s),int(l),int(d))
    dicio['cliente']=c
    dicio['numero']=int(n)
    dicio['saldo']=int(s)
    dicio['limite']=int(l)
    dicio['debito']=int(d)
    for k,v in dicio.items():
        print(f'{k}={v}')
    Label(text=f'{obj1} ').place(x=250,y=80)

    
def DEPOSITAR():
    pass
   


j=Tk()
j.geometry('300x300')


Label(text='CLIENTE :').place(x=10,y=20)
Label(text='NÚMERO :').place(x=10,y=60)
Label(text='SALDO:').place(x=10,y=100)
Label(text='LIMITE:').place(x=10,y=140)
Label(text='DEBITO:').place(x=10,y=180)

cliente=Entry(j)
cliente.place(x=75,y=20)

numero=Entry(j)
numero.place(x=75,y=60)

saldo=Entry(j)
saldo.place(x=75,y=100)

limite=Entry(j)
limite.place(x=75,y=140)

debito=Entry(j)
debito.place(x=75,y=180)

criar=Button(j,text='CRIAR OBJETO',command=criar)
criar.place(x=50,y=220)

Label(text='ESCOLHA A CONTA PARA O DEPOSITO :').place(x=10,y=300)
escolha_conta=Entry(j)
escolha_conta.place(x=230,y=300)

Label(text='VALOR DO DEPÓSITO :').place(x=10,y=340)
valor_d=Entry(j)
valor_d.place(x=150,y=340)

dpst=Button(j,text='DEPOSITAR',command=DEPOSITAR )
dpst.place(x=50,y=380)





j.mainloop()


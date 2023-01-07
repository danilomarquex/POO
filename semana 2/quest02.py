class Bicicleta():
    #atributos
    peso=None
    altura=None
    veloc_atual=0
    cor=None
    aro=None
    altura_cela=0
    calibragem_pneu=0
    veloc_max=None
    veloc_min=0
    
    #metodos
    
    def pedalar(self):
        if 0<=self.veloc_atual<=(self.veloc_max-1):
            self.veloc_atual+=1
            print("Velocidade Atual: {}".format(self.veloc_atual))
            
    def freiar(self):
        if self.veloc_atual>0:
            self.veloc_atual-= 1
            print("Velocidade da bicicleta após freiar: {}".format(self.veloc_atual))
        
    def ajustar_cela(self,valor):
        if self.veloc_atual==0:
            if 0<=valor<=5:
                self.altura_cela=valor
                print("altura atual da cela: {}".format(self.altura_cela))
                
    def calibrar_pneu(self,valor):
        if self.veloc_atual==0:
            if 0<=valor<=30:
                self.calibragem_pneu=valor
                print("altura atual da cela: {}".format(self.calibragem_pneu))
                

bicicleta1 = Bicicleta()
bicicleta1.peso=50
bicicleta1.altura=1
bicicleta1.aro=20
bicicleta1.cor="preto"
bicicleta1.veloc_max=80
bicicleta1.pedalar()
bicicleta1.ajustar_cela(4)
bicicleta1.calibrar_pneu(20)
bicicleta1.freiar()
bicicleta1.ajustar_cela(4)
bicicleta1.calibrar_pneu(20)
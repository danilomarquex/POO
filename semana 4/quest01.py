class Bicicleta:
    # atributos
    def __init__(self, peso, altura, cor, aro):
        self.peso = peso
        self.altura = altura
        self.veloc_atual = 0
        self.cor = cor
        self.aro = aro
        self.altura_cela = 0
        self.calibragem_pneu = 0
        self.veloc_max = None
        self.veloc_min = 0
    
    # metodos
    def pedalar(self):
        if 0<=self.veloc_atual<=(self.veloc_max-1):
            self.veloc_atual+=1
            print("Velocidade Atual: {}km/h".format(self.veloc_atual))
            
    def freiar(self):
        if self.veloc_atual>0:
            self.veloc_atual-= 1
            print("Velocidade da bicicleta após freiar: {}km/h".format(self.veloc_atual))
        else:
            print('Impossível freiar, pois a bicicleta já está parada!')
        
    def ajustar_cela(self,valor):
        if self.veloc_atual==0:
            if 0<=valor<=5:
                self.altura_cela=valor
                print("altura atual da cela: {}".format(self.altura_cela))
                
    def calibrar_pneu(self,valor):
        if self.veloc_atual==0:
            if 0<=valor<=30:
                self.calibragem_pneu=valor
                print("Calibragem atual do Pneu: {}".format(self.calibragem_pneu))

# instanciando objetos
bicicleta1 = Bicicleta(54, 1.70, 'amarela', 20)
print('A cor da bicicleta é {}'.format(bicicleta1.cor))
print('O peso da bicicleta é {}'.format(bicicleta1.peso))
print('A altura da bicicleta é {}'.format(bicicleta1.altura))
print('O Aro da bicicleta é {}'.format(bicicleta1.aro))
bicicleta1.veloc_max = 80
bicicleta1.pedalar()
bicicleta1.pedalar()
bicicleta1.pedalar()
bicicleta1.pedalar()
bicicleta1.freiar()
bicicleta1.freiar()
bicicleta1.ajustar_cela(4)
bicicleta1.calibrar_pneu(20)
bicicleta1.ajustar_cela(4)
bicicleta1.calibrar_pneu(20)

print('=' *60)

bicicleta2 = Bicicleta(70, 2, 'Preta', 24)
print('A cor da bicicleta é {}'.format(bicicleta2.cor))
print('O peso da bicicleta é {}'.format(bicicleta2.peso))
print('A altura da bicicleta é {}'.format(bicicleta2.altura))
print('O Aro da bicicleta é {}'.format(bicicleta2.aro))
bicicleta2.veloc_max = 80
bicicleta2.pedalar()
bicicleta2.pedalar()
bicicleta2.pedalar()
bicicleta2.freiar()
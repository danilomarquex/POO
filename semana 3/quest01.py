class Televisão:
    # Construtor da classe
    def __init__(self):
        self.ligada = 'desligada'
        self.canal = None
        self.canal_min = 2
        self.canal_max = 130
        self.volume = None
        self.volume_min = 0
        self.volume_max = 99
        self.tvnome = None

    def checa_volume_min(self):
        if self.volume == self.volume_min:
            print('Volume mínimo atingido!')
            return True
        return False
    
    def ligar(self):
        if self.ligada == 'desligada':
            self.ligada = 'ligada'
            print('A {} está {}!!' .format(self.tvnome, self.ligada))

    def desligar (self):
        if self.ligada == 'ligada':
            self.ligada = 'desligada'
            print('A {} está {}!!' .format(self.tvnome, self.ligada))
    
    def mudar_canal (self, valor):
        if self.ligada == 'ligada':  
            if valor in range(self.canal_min,self.canal_max+1):
                self.canal = valor
                print('A {} está no canal {}!!' .format(self.tvnome, self.canal))
        else:
            print('Canal inválido!!')
    
    def aumentar_canal (self):
        if self.ligada == 'ligada':
            for i in range (2):
                self.volume += 1
            print('O canal da {} foi aumentado para {}' .format(self.tvnome, self.canal)) 
        else:
            print("Impossível aumentar o canal, pois a {} está desligada!" .format(self.tvnome))

    def diminuir_canal (self):
        if self.ligada:
            if self.canal+1 in range(self.canal_min,self.canal_max+1):
                self.canal-=1 
        print('O canal da {} agora é {}' .format(self.tvnome, self.canal))
    
    def aumentar_volume(self):
        for i in range (2):
            self.volume += 1
        print('Volume da {} aumentado para {}' .format(self.tvnome, self.volume)) 

    def diminuir_volume(self):
        if self.checa_volume_min():
            return
        self.volume -= 1
        print('Volume da {} foi diminuido para {}' .format(self.tvnome, self.volume))
    
    def mudar_volume(self, valor):
        if self.ligada:
            if valor in range(self.volume_min,self.volume_max+1):
                self.volume = valor 
                print("Volume da {} está em {}!" .format(self.tvnome, self.volume))
            else:
                print("volume inválido!")
        else:
            print("Operação não realizada. Tv está desligada!")


Televisão_do_Quarto = Televisão()
Televisão_do_Quarto.tvnome = 'TV do Quarto'
Televisão_do_Quarto.ligar()
Televisão_do_Quarto.mudar_canal(13)
Televisão_do_Quarto.mudar_volume(50)
Televisão_do_Quarto.diminuir_canal()
for i in range (3):
    Televisão_do_Quarto.diminuir_volume()
Televisão_do_Quarto.desligar()
Televisão_do_Quarto.aumentar_canal()

print('=' *60)

Televisão_da_Sala = Televisão()
Televisão_da_Sala.tvnome = 'TV da Sala'
Televisão_da_Sala.ligar()
Televisão_da_Sala.mudar_canal(7)
Televisão_da_Sala.mudar_volume(10)
Televisão_da_Sala.aumentar_volume()
Televisão_da_Sala.mudar_canal(120)
for i in range (15):
    Televisão_da_Sala.diminuir_volume()
Televisão_da_Sala.desligar()
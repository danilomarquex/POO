class Televisão:
    # Construtor da classe
    def __init__(self):
        self.ligada = 'desligada'
        self.canal = 1
        self.canal_min = 1
        self.canal_max = 130
        self.volume = 0   #== mudo
        self.volume_min = 0
        self.volume_max = 99
        self.tvnome = None

    # def checa_volume_min(self):
    #     if self.volume == self.volume_min:
    #         print('Volume mínimo atingido!')
    #         return True
    #     return False
    
    def ligar(self):
        if self.ligada == 'desligada':
            self.ligada = 'ligada'
            self.canal = self.canal_min
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
    
    def aumentar_canal (self, valor=1):
        if self.ligada == 'ligada':
            if self.canal_min < self.canal+valor:
                if self.canal_max > self.canal+valor:
                    for i in range (valor):
                        self.canal += 1
                    print('O canal da {} foi aumentado para {}' .format(self.tvnome, self.canal))
                else:
                    print('Limite máximo de canal atingido!') 
            else:
                print('Canal mínimo atingido!!!')
        else:
            print("Impossível aumentar o canal, pois a {} está desligada!" .format(self.tvnome))

    def diminuir_canal (self, valor=1):
        if self.ligada == 'ligada':
            if self.canal_min < self.canal+valor:
                if self.canal_max > self.canal+valor:
                    for i in range (valor):
                        self.canal -= 1
                    print('O canal da {} foi diminuido para {}' .format(self.tvnome, self.canal))
                else:
                    print('Limite máximo de canal atingido!') 
            else:
                print('Canal mínimo atingido!!!')
        else:
            print("Impossível diminuir o canal, pois a {} está desligada!" .format(self.tvnome))

    def aumentar_volume (self, valor=1):
        if self.ligada:
            if self.volume_min < self.volume+valor:
                if self.volume_max > self.volume+valor:
                    for i in range (valor):
                        self.volume += 1
                    print('O volume da {} foi aumentado para {}' .format(self.tvnome, self.volume))
                else:
                    print('Limite máximo de volume atingido!') 
            else:
                print('Limite mínimo de volume atingido!!!')
        else:
            print("Impossível aumentar o volume, pois a {} está desligada!" .format(self.tvnome))

    def diminuir_volume (self, valor=1):
        if self.ligada:
            if self.volume_min < self.volume+valor:
                if self.volume_max > self.volume+valor:
                    for i in range (valor):
                        self.volume -= 1
                    print('O volume da {} foi diminuido para {}' .format(self.tvnome, self.volume))
                else:
                    print('Limite máximo de volume atingido!') 
            else:
                print('Limite mínimo de volume atingido!!!')
        else:
            print("Impossível diminuir o volume, pois a {} está desligada!" .format(self.tvnome))

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
Televisão_do_Quarto.aumentar_canal()
Televisão_do_Quarto.diminuir_canal() 
Televisão_do_Quarto.aumentar_volume(4)   
Televisão_do_Quarto.diminuir_volume()
Televisão_do_Quarto.desligar()
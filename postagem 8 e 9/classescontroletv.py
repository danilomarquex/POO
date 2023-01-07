class Televisao:
    
    def __init__(self, volume_atual = 5, volume_max = 100, volume_min = 0, canal_max = 150, canal_min = 2, canal_atual = None, ligada = False):
        self.__ligada = ligada
        self.__canal_atual = canal_atual
        self.__canal_min = canal_min
        self.__canal_max = canal_max
        self.__volume_min = volume_min
        self.__volume_max = volume_max
        self.__volume_atual = volume_atual

    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, ligada):
        self.__ligada=ligada   

    @property
    def canal_atual(self):
        return self.__canal_atual

    @canal_atual.setter
    def canal_atual(self, canal_atual):
        self.__canal_atual=canal_atual
        
    @property
    def volume_atual(self):
        return self.__volume_atual

    @volume_atual.setter
    def volume_atual(self, volume_atual):
        self.__volume_atual=volume_atual

    @property
    def canal_max(self):
        return self.__canal_max

    @canal_max.setter
    def canal_max(self, canal_max):
        self.__canal_max=canal_max

    @property
    def canal_min(self):
        return self.__canal_min

    @canal_min.setter
    def canal_min(self, canal_min):
        self.__canal_min=canal_min

    @property
    def volume_max(self):
        return self.__volume_max

    @volume_max.setter
    def volume_max(self, volume_max):
        self.__volume_max = volume_max

    @property
    def volume_min(self):
        return self.__volume_min

    @volume_min.setter
    def volume_min(self, volume_min):
        self.__volume_min = volume_min

    def ligar_Tv(self):
        if self.ligada == False:
            self.__ligada = True
            print("a tv foi ligada")
        else:
            print('A TV ja esta ligada!')

    def desligar_Tv(self):
        if self.ligada == True:
            self.__ligada = False
            print("a tv foi desligada")
        else:
            print('A Tv já está desligada!')

    def mudar_canal(self, valor):
        if self.ligada == True:  
            self.__canal_atual = valor
            print("Canal alterado para: {}" .format(self.__canal_atual))
        else:
            print('Não é possível mudar o canal, pois a Tv está desligada!!')

    def aumentar_volume(self):
        if self.ligada == True:
            self.__volume_atual += 1
            print("Volume aumentado para: {}" .format(self.__volume_atual))
        else:
            print('Não é possível aumentar o volume, pois a Tv está desligada!!')

    def abaixar_volume(self):
        if self.ligada == True:
            self.__volume_atual -= 1
            print("Volume diminuido para: {}".format(self.__volume_atual))
        else:
            print('Não é possível abaixar o volume, pois a Tv está desligada!!')

class Controle_remoto:
    def __init__(self, ligado = False, tv = None):
        self.__ligado = ligado
        self.__tv = tv
    
    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, ligadodesligado):
        self.__ligado = ligadodesligado

    @property
    def tv(self):
        return self.__tv
    
    @tv.setter
    def tv(self, tv):
        self.__tv = tv

    def ligar_desligar(self):
        if self.ligado == False:
            self.__ligado = True
            print('Controle ligado!')
        elif self.ligado == True:
            self.__ligado == False
            print('O controle foi desligado!')

    def vincular_tv(self, tv):
        if self.ligado == True:
            if self.tv == None:
                print('A tv foi vinculada!')
            else:
                print('Controle já vinculado a uma TV!')
        else:
            print('Ação não executada, ligue o controle primeiro!!')

    def desvincular_tv(self):
        if self.ligado == True:
            if self.tv != None:
                self.__tv = None
                print('A tv foi desvinculada!')
            else:
                ('Nenhuma tv foi vinculada ainda!')
        else:
            print('Ação não executada, ligue o controle primeiro!!')
    
    def ligar_tv(self):
        if self.ligado == False:
            print("Primeiro ligue o controle para executar esta ação!")
        elif self.tv == None:
            print("A tv não está vinculada!!")
        else:
            self.tv.ligar_Tv()
    
    def desligar_tv(self):
        if self.ligado == False:
            print("O controle esta desligado!")
        elif self.__tv == None:
            print("A tv não está vinculada ao controle!!")
        else:
            self.tv.desligar_Tv()

    def aumentar_volume_tv(self):
        if self.ligado==False:
            print("o comtrole esta desligado!!")
        elif self.tv==None:
            print("a tv não esta vinculada no controle")
        elif self.tv.volume_atual==100:
            print("volume maximo alcançado")
        else:
            self.tv.aumentar_volume()
    
    def abaixar_volume_tv(self):
        if self.ligado == False:
            print("O comtrole está desligado!!")
        elif self.tv == None:
            print("A tv não esta vinculada ao controle!!!")
        elif self.tv.volume_atual==2:
            print("Volume mínimo alcançado!!")
        else:
            self.tv.abaixar_volume()
    
    def mudar_canal_tv(self, valor):
        if self.ligado == False:
            print("O controle ainda está desligado!!!")
        elif self.tv == None:
            print("A tv ainda não esta vinculada no controle!!!")
        elif valor < self.tv.canal_min or valor > self.tv.canal_max:
            print("Canal inválido!!")
        else:
            self.tv.mudar_canal(valor)
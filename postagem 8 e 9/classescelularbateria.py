class Bateria:
    def __init__(self, codigo, capacidade, percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo_novo):
        self.__codigo = codigo_novo

    @property
    def capacidade(self):
        return self.__capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade_nova):
        self.__capacidade = capacidade_nova

    @property
    def percentual_carga(self):
        return self.__percentual_carga

    @percentual_carga.setter
    def percentual_carga(self, percentual_novo):
        self.__percentual_carga = percentual_novo

    def carregar(self, valor):
        if self.percentual_carga + valor < 100:
            self.__percentual_carga += valor
            print('Carga da bateria carregada para {}%' .format(self.percentual_carga))
        else:
            self.__percentual_carga = 100
            print('A bateria já está carregada {}%!!' .format(self.percentual_carga))
    
    def descarregar(self, valor):
        if self.percentual_carga - valor > 0:
            self.__percentual_carga -= valor
            print('Bateria descarregada para {}%!!' .format(self.percentual_carga))
        else:
            self.__percentual_carga = 0
            print('Bateria totalmente descarregada, percentual: {}%' .format(self.percentual_carga))
    
class Celular:
    def __init__(self, imei, bateria = None, ligado = False, wifi = False):
        self.__imei = imei
        self.__bateria = bateria
        self.__ligado = ligado
        self.__wifi = wifi

    @property
    def imei(self):
        return self.__imei

    @imei.setter
    def imei(self, imei_novo):
        self.__imei = imei_novo

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, bateria_nova):
        self.__bateria = bateria_nova

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, x):
        self.__ligado = x

    @property
    def wifi(self):
        return self.__wifi

    @wifi.setter
    def wifi(self, wifi_novo):
        self.__wifi = wifi_novo

    def ligar_desligar(self):
        if self.ligado == False:
            self.__ligado = True
            print('Celular ligado!!')
        elif self.bateria == None:
            print('Celular sem bateria!!')
        elif self.bateria.percentual_carga == 0:
            print('Celular descarregado!!')
        else:
            self.ligado = False
            print('Celular desligado!')

    def colocar_bateria(self, bateria):
        if self.bateria == None:
            self.__bateria = bateria
            print('Bateria adicionada ao celular!!')
        else:
            print('O dispositivo já possui uma bateria!!')

    def retirar_bateria(self):
        if self.bateria != None:
            self.__bateria == None
            print('Bateria do celular removida!!')
        else:
            print('Celular sem bateria!!')
    
    def ligar_desligar_wifi(self):
        if self.wifi == False:
            self.__wifi = True
            print('O wifi foi ligado!!')
        else:
            self.__wifi = False
            print('O Wifi foi desligado!!')

    def assistir_video(self, tempo):
        if self.ligado == False:
            print('Celular desligado!')
        elif self.bateria == None:
            print('O celular está sem bateria!!')
        elif self.wifi == False:
            print('O Wifi está desligado!!')
        else:
            self.bateria.descarregar(tempo*5)
    
    def carregar_celular(self, valor):
        if self.bateria == None:
            print('O celular está sem bateria!!')
        elif self.bateria.percentual_carga == 100:
            print('Celular totalmente carregado!!')
        else: 
            self.bateria.carregar(valor)

    def descarregar(self, valor):
        if self.bateria == None:
            print('Celular sem bateria!!')
        elif self.bateria.percentual_carga == 0:
            print('O celular está totalmente descarregado!!')
        else:
            self.bateria.descarregar(valor)
    

class Casa:
    def __init__(self, localizacao, area_total, area_construida, porta_frente = None, porta_fundo = None):
        self.__localizacao = localizacao
        self.__area_total = area_total
        self.__area_construida = area_construida
        self.__porta_frente = porta_frente
        self.__porta_fundo = porta_fundo
    
    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, valor):
        print('sem permição!!')

    @property
    def area_total(self):
        return self.__area_total

    @area_total.setter
    def area_total(self, valor):
        print('sem permissao!!')

    @property 
    def area_construida(self):
        return self.__area_construida

    @area_construida.setter
    def area_construida(self, valor):
        print('sem permissao!!')

    @property 
    def porta_frente(self):
        return self.__porta_frente

    @porta_frente.setter
    def porta_frente(self, valor):
        print('sem permissão!!')

    @property
    def porta_fundo(self):
        return self.__porta_fundo

    @porta_fundo.setter
    def porta_fundo(self, valor):
        print('sem permissão!!')

    def trocar_porta(self, porta, valor):
        if porta == 1 and type(valor)==Porta:
            self.__porta_frente = valor
        elif porta == 2 and type(valor)==Porta:
            self.__porta_fundo = valor
        else:
            print("valores errados")
    def __str__(self):
        return "Casa:\n{} \n{} \n{} \n{} \n{}\n".format(self.localizacao,self.area_total,self.area_construida,self.porta_frente, self.porta_fundo)


class Porta:

    def __init__(self, cor = "marrom", tipo = "madeira", altura = 5, largura = 2, esta_fechada = True, esta_trancada = True):
        self.__cor = cor
        self.__tipo = tipo
        self.__altura = altura
        self.__largura = largura
        self.__esta_fechada = esta_fechada
        self.__esta_trancada = esta_trancada

    @property
    def cor(self):
        return self.__cor 

    @cor.setter
    def cor(self, valor):
        print('sem permissão!!')

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        print('sem permissão!!')
    
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        print('sem permissão!!')

    @property
    def largura(self):
        return self.__largura

    @altura.setter
    def altura(self, valor):
        print('sem permissão!!')

    @property
    def esta_fechada(self):
        return self.__esta_fechada

    @esta_fechada.setter
    def esta_fechada(self, valor):
        print('sem permissão')

    @property
    def esta_trancada(self):
        return self.__esta_trancada
    
    @esta_trancada.setter
    def esta_trancada(self, valor):
        print('sem permissão')

    def abrir(self):
        if self.__esta_trancada:
            print("Não é possivel abrir, a porta esta trancada")
        else:
            self.__esta_fechada = False

    def Fechar(self):
        self.__esta_fechada = True
        print('porta fechada')

    def Trancar(self):
        if self.__esta_fechada == False:
            print("Não é possivel trancar, a porta está aberta")
        else:
            self.__esta_trancada = True
            print('porta trancada')

    def Destrancar(self):
        self.__esta_trancada = False
        print('porta destrancada')
    
    def __str__(self):
        return "Porta:\n{} \n{} \n{} \n{} \n{}\n{}\n".format(self.esta_fechada,self.esta_trancada,self.cor,self.tipo,self.altura,self.largura)
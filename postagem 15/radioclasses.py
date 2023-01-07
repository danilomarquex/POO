class Radio:
    def __init__(self, volume, nome='',marca='',status = False,faixas_fm = None,faixa_atual = None):
        self.__volume = volume
        self.__nome = nome
        self.__marca = marca
        self.__status = status
        self.__faixas_fm = faixas_fm
        self.__faixa_atual = faixa_atual

    @property
    def nome(self):
        return self.__nome
    @property
    def marca(self):
        return self.__marca
    @property
    def status(self):
        return self.__status
    @property
    def volume(self):
        return self.__volume
    @property
    def faixas_fm(self):
        return self.__faixas_fm
    @property
    def faixa_atual(self):
        return self.__faixa_atual

    @faixas_fm.setter
    def faixas_fm(self,v):
        self.__faixas_fm = v
    @faixa_atual.setter
    def faixa_atual(self,v):
        self.__faixa_atual = v

    def Ligar_desligar(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
    
    def Ajustar_volume(self,valor=1):
        self.__volume += valor
        self.__volume == max(min(self.__volume,100),0)
        print('o volume agora está em ',self.__volume)
    
    def Sintonizar_freq(self,freq):
        for i in self.__faixas_fm.fms:
            if freq == i.frequencia:
                return i
        return self.faixas_fm.fms.index(self.__faixa_atual)+1
    
    def Sintonizar_estilo(self,est):
        for i in self.__faixas_fm.fms:
            if est == i.estilo_musica:
                return i
        return None

    def Mostrar_display(self):
        print(self)

    def __str__(self):
        if self.__status == True:
            return '{}\n< {} >\nFrequencia: {}\nMusica: {}\nVolume: {}'.format('='*10,self._faixa_atual.nome,self.faixa_atual.frequencia,self.faixa_atual.musica_atual,self._volume)
        else:
            return 'esta desligado'
            
class Estacoes_FM:
    def __init__(self, fms = ""):
        self.__fms = fms
    @property
    def fms(self):
        return self.__fms

    @fms.setter
    def fms(self,v):
        self.__fms = v

    def Atualizar_fm(self,inst,musica,estilo,freq=None,nom=None):
        inst.musica_atual = musica
        inst.estilo_musica = estilo
        if freq != None:
            inst.frequencia = freq
        if nom != None:
            inst.nome = nom
    
    def Consultar_fm(self,fm):
        if type(fm) == str:
            for i in self.__fms:
                if fm == i.nome:
                    return  i
            return None
        elif type(fm) == int:
            for i in self.__fms:
                if fm == i.frequencia:
                    return i
            return None
    
    def Cadastrar_fm(self,v):
        self.__fms.append(v)
    
    def Excluir_fm(self,v):
        self.__fms.remove(v)

class Estacao_FM:
    def __init__(self,frequencia,nome,status,musica_atual,estilo_musica):
        self.__frequencia = frequencia
        self.__nome = nome
        self.__status = status
        self.__musica_atual = musica_atual
        self.__estilo_musica = estilo_musica

    @property
    def frequencia(self):
        return self.__frequencia
    @property
    def nome(self):
        return self.__nome
    @property
    def status(self):
        return self.__status
    @property
    def musica_atual(self):
        return self.__musica_atual
    @property
    def estilo_musica(self):
        return self.__estilo_musica

    @frequencia.setter
    def frequencia(self,v):
        self.__frequencia = v
    @nome.setter
    def nome(self, v):
        self.__nome = v
    @status.setter
    def status(self, v):
        self.__status = v
    @musica_atual.setter
    def musica_atual(self, v):
        self.__musica_atual = v
    @estilo_musica.setter
    def estilo_musica(self, v):
        self.__estilo_musica = v

    def Entrar_no_ar(self):
        self.__status = True
    def Sair_do_ar(self):
        self.__status = False

    def Atualiza_musica(self,nom,est):
        self.__musica_atual = nom
        self.__estilo_musica = est
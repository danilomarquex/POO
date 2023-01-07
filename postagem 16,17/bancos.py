class Conta_corrente: 
    def __init__(self, numero, saldo):
        self.numero = numero  
        self.saldo = saldo

    def __str__(self):
        return " Numero da conta: {} \n Saldo: {} " .format(self._numero, self._saldo)
    
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def creditar(self, valor):
        self._saldo += valor

    def debitar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print(' Débito não autorizado, pois você não possui esse valor em conta! ')

    def transferir(self, valor, conta_destino, conta_saida):
        if valor <= conta_saida.saldo:
            conta_saida.debitar(valor)
            conta_destino.creditar(valor)
            print(' Tranferência efetuada no valor de R${} para {}!' .format(valor, conta_saida.numero))

class Conta_poupanca(Conta_corrente):
    def __init__(self, numero, saldo, taxa_juros):
        super().__init__(numero, saldo)
        self.__taxa_juros = taxa_juros

    def __str__(self):
        return super().__str__()+"\n Taxa de juros:{}" .format(self.__taxa_juros)
    
    @property
    def taxa_juros(self):
        return self.__taxa_juros
    @taxa_juros.setter
    def taxa_juros(self, valor):
        self.__taxa_juros = valor

    def render_juros(self):
        txj = self.__taxa_juros
        valor_ajustado = (((txj/100) * self._saldo) + self._saldo)
        self.__saldo = valor_ajustado
        print(' Valor ajustado: {}' .format(self._saldo))

class Conta_imposto(Conta_corrente):
    def __init__(self, numero, saldo, percentual_imposto):
        super().__init__(numero, saldo)
        self.__percentual_imposto = percentual_imposto
    
    @property
    def percentual_imposto(self):
        return self.__percentual_imposto
    @percentual_imposto.setter
    def percentual_imposto(self, valor):
        self.__percentual_imposto = valor

    def calcula_imposto(self):
        imposto = (self._saldo * (self.__percentual_imposto/100))
        saldo_atualizado = (self._saldo - imposto)
        print(' Saldo atualizado: {}' .format(saldo_atualizado))

    def __str__(self):
        imposto = (self._saldo * (self.__percentual_imposto/100))
        saldo_atualizado = (self._saldo - imposto)
        return super().__str__() + '\n' + '\n Percentual do Imposto: {}\n Saldo Atual: {}' .format(self.__percentual_imposto, saldo_atualizado) 
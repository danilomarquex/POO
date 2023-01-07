class Data(object):
    def inicializa(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def mostra(self):
        print("Data:",self.dia,"/",self.mes,"/", self.ano)
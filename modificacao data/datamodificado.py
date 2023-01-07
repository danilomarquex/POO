# Data modificado com os métodos init e str

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def __str__(self):
        return "Data: {}/{}/{}" .format(self.dia, self.mes, self.ano)

# Execução >>>

datatest = Data(26, 3, 2005)
print(datatest)
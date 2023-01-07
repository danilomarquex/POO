class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return "Marca: {} \nModelo: {} \nAno: {}" .format(self.marca, self.modelo, self.ano)

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
        


    def __str__(self):
        return super().__str__()
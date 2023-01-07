class Mamiferos:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    # def __str__(self):
        # return " Nome: {} \n Idade: {}" .format(self.nome, self.idade)

class Cachorro(Mamiferos):
    def __init__(self, nome, idade, raça, late):
        super().__init__(nome, idade)
        self.raça = raça
        self.late = late #Boll, True or False
    # def __str__(self):
        # return super().__str__() + "\n Late: {} \n Raça: {}" .format(self.raça, self.late)

class Macaco(Mamiferos):
    def __init__(self, nome, idade, sobe_em_arvores, raça):
        super().__init__(nome, idade)
        self.sobe_em_arvores = sobe_em_arvores # True or False
        self.raça = raça
    # def __str__(self):
        # return super().__str__() + "\n Sobe em arvores? {} \n Raça: {}" .format(self.sobe_em_arvores, self.raça)

class Homem(Mamiferos):
    def __init__(self, nome, idade, fala):
        super().__init__(nome, idade)
        self.fala = fala #True or False
    #  def __str__(self):
        # return super().__str__() + "\n Fala? {}" .format(self.fala)
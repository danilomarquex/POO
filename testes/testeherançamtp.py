class Homem(object):
    def __init__(self, linguagem):
        super().__init__()
        self.linguagem = linguagem
    def __str__(self) -> str:
        return ' Linguagem: {}' .format(self.linguagem)

class Aranha(object):
    def __init__(self, teia, venenosa):
        super().__init__()
        self.teia = teia
        self.venenosa = venenosa
    def __str__(self) -> str:
        return ' Teia: {} \n Venenosa: {}' .format(self.teia, self.venenosa)

class HomemAranha(Homem, Aranha):
    def __init__(self, linguagem, teia, venenosa):
        super().__init__(linguagem = linguagem, teia = teia, venenosa = venenosa)
    def __str__(self) -> str:
        return super().__str__() + ' Linguagem: {} \n Teia: {} \n venenosa: {}' .format(self.linguagem, self.teia, self.venenosa)

ha = HomemAranha('Ingles', True, False)
print(ha)
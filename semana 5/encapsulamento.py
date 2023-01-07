class Pessoa:
    def __init__ (self, nome, peso):
        self.__nome = nome
        self.__peso = peso

    def getnome(self):
        return self.__nome
    
    @property
    def peso(self):
        return self.__peso

eu = Pessoa("()SS", 50)
print(eu.getnome())
print(eu.peso)

# vou te mostrar como instalar a extensão do python aqui no VSCode

#aí tu instala :3
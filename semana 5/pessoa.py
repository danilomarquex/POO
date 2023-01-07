class Pessoa:
    
    def __init__(self, nome, idade, peso, altura):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura 
        self.__estado = True   # True = 'Vivo' /// False = 'Morto'
        self.__estado_civil = 'solteiro'
        self.__conjugue = None

    def get_estado_civil(self):
        return self.__estado_civil

    def set_estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil

    def get_conjugue(self):
        if self.__conjugue:
            return self.__conjugue.name
        return self.__conjugue

    def set_conjugue(self, conjugue):
        self.__conjugue = conjugue

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade
    
    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura
    
    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def envelhecer(self):
        idade = self.get_idade()
        if idade < 21:
            altura = self.get_altura()
            self.set_altura(altura + 0.5)
        self.set_idade(idade + 1)
        return

    def crescer(self, valor):
        idade = self.get_idade()
        if idade <= 21:
            altura = self.get_altura()
            self.set_altura(altura + valor)
        return

    def engordar(self, valor):
        peso = self.get_peso()
        self.set_peso(peso + valor)
        return

    def emagrecer(self, valor):
        peso = self.get_peso()
        self.set_peso(peso - valor)
        return


# INSTANCIA DOS OBJETOS
eu = Pessoa("Danilo", 16, 55, 1.70)
print(eu.get_nome())
print(eu.get_idade())
print(eu.get_peso())
print(eu.get_estado())

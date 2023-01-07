class Escritor:
    def __init__(self, nome):
        self.nome = nome
    
    @property
    def nome(self):
        print('getting values')
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print('setting value')
        self.__nome = nome

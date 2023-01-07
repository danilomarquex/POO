class Primeiro(object):
    def __init__(self):
        print("Primeiro...")
        super().__init__()    

class Segundo(object):
    def __init__(self):
        print("Segundo...")
        super().__init__()       

class Terceiro(Primeiro,Segundo):
    def __init__(self):
        print("terceiro...")
        super(Terceiro,self).__init__()     
    
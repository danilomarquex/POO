class Formas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Quadrado(Formas):
    def __init__(self, x, y):
        super().__init__(x,y)

    def area(self):
        return self.x * self.y

class Circulo(Formas):
    def __init__(self, x, y):
        super().__init__(x, y)

    def area(self):
        return 3.14 * self.x * self.y

class Retangulo(Formas):
    def __init__(self, x, y):
        super().__init__(x,y)

    def area(self):
        return self.x*self.y


q1 = Quadrado(3, 3)
print('A área do Quadrado é {}!' .format(q1.area()))

c1 = Circulo(2, 2)
print('A área do Círculo é {}!' .format(c1.area()))

r1 = Retangulo(4, 6)
print('A áread do Retangulo é {}!' .format(r1.area()))
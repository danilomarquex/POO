from mamiferos import Mamiferos
from mamiferos import Cachorro
from mamiferos import Macaco
from mamiferos import Homem

print('<<<mamiferos>>>')
mam01 = Mamiferos('Bob', 7)
print(mam01)


print('<<<cachorro>>>')
dog01 = Cachorro('Marley', 9, True,'Vira-lata')
print(dog01)


print('<<<macaco>>>')
monkey01 = Macaco('Gorilla', 9, True, 'Sagui')
print(monkey01)

print('<<<homem>>>')
man = Homem('Pedro', 19, False)
print(man)
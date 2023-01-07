from cliente import Cliente
from cliente import Cliente_Fisico
from cliente import Cliente_Juridico

print('<<<cliente>>>')
cli01 = Cliente(57745, "Rio de Janeiro")
print(cli01)


print('<<<cliente_físico>>>')
clifi01 = Cliente_Fisico('Danilo', 1234322, 1244534, "Teresina")
print(clifi01)

print('<<<cliente_jurídico>>>')
clijur = Cliente_Juridico(4232242, 'Teresina - PI', 58749374, )
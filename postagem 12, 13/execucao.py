from classesbancocontacliente import Banco
from classesbancocontacliente import Conta
from classesbancocontacliente import Cliente

# <<<testando>>>

# bancos
bradesco = Banco('Bradesco')
nubank = Banco('Nubank')
bb = Banco('Banco do Brasil')

# contas
conta01 = Conta('Danilo', 4338, 250)
conta02 = Conta('Lana', 1313, 75)
conta03 = Conta('Rita', 1919, 50)
conta04 = Conta('Junior', 2098, 1050)
conta05 = Conta('Marinalva', 7755, 204)
conta06 = Conta('Geovana', 1242, 532)

# clientes
rita = Cliente(191960, "Rita Guimarães")
geovana = Cliente(124308, "Geovana Silva")
marinalva = Cliente(445512, "Marinalva Marques")

# teste do método 'adicionar'
nubank.adicionar(conta01)
nubank.adicionar(conta03)
bradesco.adicionar(conta02)
bradesco.adicionar(conta04)
bb.adicionar(conta05)
bb.adicionar(conta06)

# teste do método 'depositar' e 'sacar'
#   Nubank
conta01.depositar(150)
conta03.sacar(20)
#   Bradesco
conta02.depositar(150)
conta04.sacar(20)

#   Banco do Brasil
conta05.sacar(30)
conta06.depositar(250)

# mostrando nomes e saldo dos bancos
print(nubank)
print(bradesco)
print(bb)

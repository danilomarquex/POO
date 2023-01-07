from conta import Conta

conta1 = Conta('Ana', 1098, 100)
# conta1.saque(120)
# conta1.deposito(50)


conta2 = Conta('Marinalva', 3539, 150)
conta2.transferir(20, conta1)

print(conta1)
print(conta2)

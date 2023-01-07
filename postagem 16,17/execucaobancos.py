from bancos import Conta_corrente, Conta_imposto, Conta_poupanca

# Instâncias
print('<<<Conta Corrente>>>')
contac01 = Conta_corrente(222, 250)
contac01.creditar(50)
contac01.debitar(20)
print(contac01)

contac02 = Conta_corrente(333, 50)
contac02.creditar(50)
contac02.debitar(30)
# Transferências
contac01.transferir(10, contac02, contac01)
print(contac02)

print()
print('<<<Conta Poupança>>>')
contap01 = Conta_poupanca(4523, 100, 50)
contap01.creditar(20)
contap01.debitar(10)
contap01.render_juros()
print(contap01)


contap02 = Conta_poupanca(5533, 50, 10)
contap02.creditar(10)
contap02.debitar(20)
# Transferências
contap01.transferir(15, contap01, contap02)

contap02.render_juros()
print(contap02)

print()
print('<<<Conta Imposto>>>')
contai01 = Conta_imposto(6655, 250, 20)
contai01.creditar(20)
contai01.debitar(15)
contai01.calcula_imposto()
print(contai01)

contai02 = Conta_imposto(7456, 350, 40)
contai02.creditar(10)
contai02.debitar(15)
# Tranferências
contai01.transferir(12, contap02, contai01)
contai02.calcula_imposto()
print(contai02)
from funcionario import Funcionario
from funcionario import Gerente
from funcionario import Secretaria

print('<<funcionários>>>')
fun01 = Funcionario("Danilo", 1679742382, 1500)
print(fun01)

print('<<<gerentes>>>')
ger01 = Gerente("Roberto", 9238848, 2050, "TMA Nordeste", 500)
print(ger01)

print('<<<Secretaria>>>')
sec01 = Secretaria('Marinalva', 465883649, 2100, "Gerencia")
print(sec01)
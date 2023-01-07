from Vacina import *

Obesidade=Comorbidade
maria = Pessoa(11111111111,"Maria","11/06/2000",30,"Obesidade")
print(maria.getIdade())
v1 = VacinaCovid(1,"Teresina","CoronaVac","08/06/2021",maria)
print(maria)
print()
Controle = ControleVacina()
Controle.incluirVacina(v1)
Controle.incluirVacina(VacinaCovid(2,"Teresina","Pfizer","08/06/2021",Pessoa(22222222222,"João","15/12/1990","Diabetes")))
Controle.incluir2doseVacina(1,'08/06/2021')
print()
joão=Pessoa(2222222222,"João","15/12/1990",31,"Diabetes")
v2 = VacinaCovid(1,"Teresina","Pfizer","08/06/2021",joão)
Controle = ControleVacina()
Controle.incluirVacina(v2)
print(joão)
print(v2)






from pessoavacina import *

Diabetes = Comorbidade

joao = Pessoa(64734, 'João', '12/12/1994', 20, 'Diabetes')

print(joao.getIdade())

vacina1 = VacinaCovid(1, 'Belo Horizonte', 'Astrazeneca', '10/07/2021', joao)
print(joao)

controle1 = ControleVacina()
controle1.incluirVacina(vacina1)
controle1.incluirVacina(VacinaCovid(2, 'Belo Horizonte', 'Astrazeneza', '10/07/2021', Pessoa(1321312, 'Rafael', '25/04/1973', 'Insuficiência cardíaca')))
controle1.incluir2doseVacina(1, '10/07/2021')
print()

lucas = Pessoa(999777, 'Lucas', '21/07/1977', 31, 'Diabetes')

vacina2 = VacinaCovid(2, 'Piauí', 'Pfizer', '10/07/2021', lucas)
controle1 = ControleVacina()
controle1.incluirVacina(vacina2)
print(lucas)
print(vacina2)
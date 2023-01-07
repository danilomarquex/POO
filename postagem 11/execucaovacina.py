from classespessoavacina import Pessoa
from classespessoavacina import vacina_covid19

danilo = Pessoa (777, "Danilo", 2005, "sim")
lana = Pessoa(2234, 'Lana', 2008, "não")
junior = Pessoa(9821, 'Junior', 1990, 'sim')
geovana = Pessoa(1588, 'Geovana', 2003, 'sim', 'diabetes')

print('<<<idade das pessoas>>>')
danilo.getIdade()
lana.getIdade()
junior.getIdade
geovana.getIdade

print('<<<Primeira dose - vacinação contra COVID-19>>>')
danilo.vacinardose1(22990, 'DF', 'AstraZeneca/Oxford')
junior.vacinardose1(1122, 'PI', 'CoronaVac')
lana.vacinardose1(9923, 'TO', 'Pfizer')
geovana.vacinardose1(9098, 'RJ', 'CoronaVac')

print('<<<Segunda dose - vacinação contra COVID-19>>>')
danilo.vacinardose2()
junior.vacinardose2()
geovana.vacinardose2()

print('<<<Dados das Pessoas>>>')
print(danilo)
print()
print(junior)
print()
print(lana)
print()
print(geovana)
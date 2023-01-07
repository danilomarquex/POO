from classes10 import Porta
from classes10 import Casa

porta1 = Porta()
porta2 = Porta()
porta3 = Porta()
porta4 = Porta()
porta5 = Porta()
porta6 = Porta()

Minha_casa = Casa('Brasilia - DF', 5, 18, porta1, porta2)
Casa_da_mae = Casa('Piracuruca', 10, 26, porta3, porta4)
Casa_dos_irmaos = Casa('Luis Correia', 15, 29, porta5, porta6)

Minha_casa.porta_frente.Fechar()
Minha_casa.porta_fundo.Trancar()

Minha_casa.trocar_porta(porta3, "Grade")
print(Minha_casa)

Casa_dos_irmaos.porta_fundo.Trancar()
Casa_dos_irmaos.porta_fundo.abrir()
Casa_dos_irmaos.porta_fundo.Destrancar
from datetime import datetime

class Relogio:
    # construtor
    def __init__(self, relogio_nome):
        self.hora_atual = None
        self.bateria = False
        self.relogio_nome = relogio_nome

    def coloca_bateria(self):
        self.bateria = True

    def ajusta_hora(self):
        if self.bateria:
            data_hora_atual = datetime.now()
            self.hora_atual = data_hora_atual.strftime('%H:%M:%S')

    def mostra_hora(self):
        if self.bateria:
            self.ajusta_hora()
            print('A hora do relógio "{}" é {} !!' .format(self.relogio_nome, self.hora_atual))


relogio_de_joao = Relogio('Rolex')
relogio_de_joao.coloca_bateria()
relogio_de_joao.mostra_hora()

relogio_de_pedro = Relogio('Lacoste')
relogio_de_pedro.coloca_bateria()
relogio_de_pedro.mostra_hora()

            
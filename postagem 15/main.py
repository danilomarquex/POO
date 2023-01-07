from radioclasses import Radio
from radioclasses import Estacoes_FM
from radioclasses import Estacao_FM

radio1 = Radio(83, 'FPS', 'Yamaha', True)

estacao01 = Estacao_FM(915, 'TwitchFM', True, "Filipe Ret - Prosperidade", "Trap")
estacao02 = Estacao_FM(911, 'SouthFM', True, 'Mumuzinho - Fulminante', 'Pagode')
estacao03 = Estacao_FM(850, 'TegaFM', True, 'MarceloD2 - Nada pode me parar', 'Samba')
estacao04 = Estacao_FM(855, 'Meio Norte', True, 'Saia Rodada - Tapão na raba', 'Piseiro')

greatseason = Estacoes_FM('estacao01, estacao02, estacao03, estacao04')

radio1.faixas_fm = greatseason

radio1.Ajustar_volume(-5)
radio1.Ajustar_volume(-20)
radio1.Ajustar_volume(8)

estacao01.Atualiza_musica("Vida Louca", "Rap")
estacao02.Atualiza_musica('Sobrevivi', 'Rap')

print(estacao01)
print()
print(estacao02)
print()
print(estacao03)
print()
print(estacao04)
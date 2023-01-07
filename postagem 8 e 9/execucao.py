from classescontroletv import Televisao
from classescontroletv import Controle_remoto

# TESTAR OS MÉTODOS NAS OUTRAS INTÂNCIAS !!!!

tv1 = Televisao(10, 100, 0, 150, 2, 5, True)
tv2 = Televisao(4, 100, 0, 150, 2, 15, False)
tv3 = Televisao(16, 100, 0, 150, 2, 22, False)

controle1 = Controle_remoto(False, tv1)
controle2 = Controle_remoto(True, tv2)
controle3 = Controle_remoto(False, tv3)

# TESTANDO MÉTODOS DA TV!!
 
tv1.ligar_Tv()
# tv1.desligar_Tv()
tv1.mudar_canal(3)
tv1.aumentar_volume()
tv1.abaixar_volume()

# TESTANDO MÉTODOS DO CONTROLE!!
controle1.ligar_desligar()
# controle1.ligar_desligar()  <<< Desligar o controle!
controle1.vincular_tv(tv1)
# controle1.desvincular_tv()
controle1.desligar_tv()
controle1.ligar_tv()
controle1.aumentar_volume_tv()
controle1.abaixar_volume_tv()
controle1.mudar_canal_tv(6)
from classescelularbateria import Bateria
from classescelularbateria import Celular

print('<<<INSTANCIAS 01>>>')
bateria1 = Bateria(9879479, 4000, 55)
bateria1.carregar(45)
bateria1.descarregar(20)

celular1 = Celular(54352, bateria1, False, True)
celular1.ligar_desligar()
celular1.colocar_bateria(bateria1)
# celular1.retirar_bateria()
# celular1.ligar_desligar_wifi() O WIFI JÁ ESTA LIGADO, SÓ OBSERVAR NOS PARÂMETROS
celular1.assistir_video(10)
celular1.carregar_celular(60)
celular1.descarregar(10)

print('<<<INSTANCIAS 02>>>')

bateria2 = Bateria(64353, 5000, 20)
bateria2.descarregar(10)
bateria2.carregar(50)

celular2 = Celular(87623, None, False, False)
celular2.colocar_bateria(bateria2)
celular2.ligar_desligar()
celular2.retirar_bateria()
celular2.ligar_desligar_wifi()
celular2.assistir_video(15)
celular2.carregar_celular(90)
celular2.descarregar(15)
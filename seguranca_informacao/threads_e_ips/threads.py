from threading import Thread
import time

#criando carro1
def carro(velocity, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocity
        time.sleep(0.5)
        print('Piloto: {} km: {} \n'.format(piloto, trajeto))

#instanciando thread
t_carro1 = Thread(target=carro, args=[1, 'bruno'])
t_carro2 = Thread(target=carro, args=[1.5, 'joao'])

#disparando thread
t_carro1.start()
t_carro2.start()
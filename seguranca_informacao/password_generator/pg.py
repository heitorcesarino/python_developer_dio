import random
import string

#tamanho da string.
size = int(input('Digite o tamanho (quantidade de caracteres) que você deseja: '))

#variavel que vai receber caracteres aleatorios.
chars = string.ascii_letters + string.digits + '!@#$&*()-=+,.;:/?'

#biblioteca random vai chamar o metodo os.urandom.
rnd = random.SystemRandom()

#printando caracteres gerados aleatorioamente respeitando o tamanho maximo definido.
print(''.join(rnd.choice(chars) for i in range (size)))
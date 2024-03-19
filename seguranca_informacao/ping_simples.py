import os #importa modulo ou biblioteca os (integra programas e recursos do sistema operacional)

print("#" * 60)

#variavel que recebe ip do usuario
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print("-" * 60)
#chamando metodo system do modulo os e chamando comando ping passando a quantidaade de pacotes a serem enviados.
os.system('ping -n 6 {}'.format(ip_ou_host)) 
print("-" * 60)
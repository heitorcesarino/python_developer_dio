import hashlib

hash_string = input("Digite o texto a ser gerado a hash: ")

opcao_menu = int(input(
    ''' ### MENU - ESCOLHA O TIPO DE HASH ###
    1 = MD5
    2 = SHA1
    3 = SHA256
    4 = SHA512
    Digite o numero do hash a ser gerado: 
    '''))

if opcao_menu == 1:
    resultado = hashlib.md5(hash_string.encode('utf-8'))
    print('A hash MD5 da string: ', hash_string, 'É: ', resultado.hexdigest())
elif opcao_menu == 2:
    resultado = hashlib.sha1(hash_string.encode('utf-8'))
    print('A hash SHA1 da string: ', hash_string, 'É: ', resultado.hexdigest())
elif opcao_menu == 3:
    resultado = hashlib.sha256(hash_string.encode('utf-8'))
    print('A hash SHA256 da string: ', hash_string, 'É: ', resultado.hexdigest())
elif opcao_menu == 4:
    resultado = hashlib.sha512(hash_string.encode('utf-8'))
    print('A hash SHA512 da string: ', hash_string, 'É: ', resultado.hexdigest())
else:
    print("Algo não aconteceu como esperado, tente novamente")
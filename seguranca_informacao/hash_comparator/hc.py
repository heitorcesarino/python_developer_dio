import hashlib

# Arquivos com frase que será utilizada para gerar o hash
archive1 = '/FORMACAO-PYTHON-DIO/seguranca_informacao/hash_comparator/a.txt'
archive2 = '/FORMACAO-PYTHON-DIO/seguranca_informacao/hash_comparator/b.txt'

# Abertura, leitura e geração do hash do archive1
hash1 = hashlib.new('ripemd160')
hash1.update(open(archive1, 'rb').read())

# Abertura, leitura e geração do hash do archive2
hash2 = hashlib.new('ripemd160')
hash2.update(open(archive2, 'rb').read())

# Comparação entre arquivos
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {archive1} é diferente do arquivo: {archive2}')
    print('o hash do arquivo a.txt é: ', hash1.hexdigest())
    print('o hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {archive1} é igual ao arquivo: {archive2}')
import itertools

#criando string que será permutada
string = input("String a ser permutada: ")

#usando o metodo da biblioteca para permutar a string, x vezes
result = itertools.permutations(string, len(string))

#loop para imprimir o resultado de cada iteração do metodo.
for i in result:
    print(''.join(i))
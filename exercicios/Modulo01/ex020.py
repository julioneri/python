from random import shuffle
a1 = str(input('Digite um aluno: '))
a2 = str(input('Digite outro aluno: '))
a3 = str(input('Digite outro aluno: '))
lista = [a1, a2, a3]
ran = shuffle(lista)
print('A ordem impregnada na lista é: {}'.format(lista))
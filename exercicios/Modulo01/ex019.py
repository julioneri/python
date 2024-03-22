from random import choice
a1 = str(input('Digite o nome de um alunos: '))
a2 = str(input('Digite o nome de outro aluno: '))
a3 = str(input('Digite o nome de outro aluno: '))
a4 = str(input ('Digite o nome de outro aluno '))
lista = [a1, a2, a3, a4]
alu = choice(lista)
print('O aluno escolhido foi: \033[35m{}\033[m'.format(alu))

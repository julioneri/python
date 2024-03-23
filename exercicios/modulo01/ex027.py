'''nome = str(input('Digite seu nome: ')).strip()
c = nome.find(' ')
f = nome.rfind(' ')
print('Seu primeiro nome é {}'.format(nome[:c]))
print('O seu último nome é{}'.format(nome[f:]))'''
nome = str(input('Digite o seu nome: ')).strip()
nome = nome.split()
print('O seu primeiro nome é \033[32m{}\033[m'.format(nome[0]))
print('O seu último nome é \033[32m{}\033[m'.format(nome[-1]))
nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem Silva? \033[32m{}\033[m'.format('SILVA' in nome.upper()))
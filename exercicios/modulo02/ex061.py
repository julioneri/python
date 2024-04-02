termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
soma = termo
print(termo, end=' > ')
while cont != 10:
    soma += razão
    print(soma, end=' > ')
    cont += 1
print('ACABOU')
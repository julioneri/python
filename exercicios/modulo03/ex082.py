lista = []
while True:
    opção = ' '
    lista.append(int(input('Digite um número: ')))
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
pares = []
ímpares = []
for d in lista:
    if d % 2 == 0:
        pares.append(d)
    elif d % 2 == 1:
        ímpares.append(d)
print('-' * 9)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {ímpares}')
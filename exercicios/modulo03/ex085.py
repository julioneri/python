lista = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    elif valor % 2 == 1:
        lista[1].append(valor)
print('=-' * 25)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[1]}')
print(f'Os valores ímpares digitados foram: {lista[0]}')

from random import randint
from time import sleep
lista = list()
print('-' * 35)
print('{: ^35}'.format('JOGA NA MEGA CENA'))
print('-' * 35)
jogos = int(input('Quantos ex107 você quer que eu sorteie? '))
print(f'-=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=-')
for c in range(1, jogos+1):
    while len(lista) != 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    print(f'Jogo {c}: {lista}')
    lista.clear()
    sleep(1)
print('-=-=-=-== < BOA  SORTE! > ==-=-=-=-')

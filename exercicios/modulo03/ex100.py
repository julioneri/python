from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        número = randint(1, 10)
        números.append(número)
        print(número, end=' ')
        sleep(.5)
    print('PRONTO!')


def somapar(list):
    soma = 0
    for n in list:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {list}, temos {soma}')


números = []
sorteia()
somapar(números)

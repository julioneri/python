from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 < n2:
    for c in range(n1, n2+1):
        sleep(.5)
        print(c, end=' ')
    print('\nContagem crescente!')
if n1 > n2:
    for c in range(n1, n2-1, -1):
        sleep(.5)
        print(c, end=' ')
    print('\nContagem regressiva!')
if n1 == n2:
    print('Os valores são iguais!')
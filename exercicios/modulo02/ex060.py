n = int(input('Digite um número para\ncalcular seu factorial: '))
c = n

"""CALCULANDO FATORIAL UTILIZANDO 'WHILE'"""
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

"""CALCULANDO FATORIAL UTILIZANDO 'FOR'"""
f = 1
print(f'Calculando {n}! = ', end='')
for fac in range(n, 0, -1):
    print(fac, end='')
    print(' x ' if fac > 1 else ' = ', end='')
    f *= fac
print(f)

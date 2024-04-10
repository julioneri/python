from random import randint
núm = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for n in núm:
    print(n, end=' ')
print(f'\nO maior valor foi {max(núm)}')
print(f'O menor valor foi {min(núm)}')

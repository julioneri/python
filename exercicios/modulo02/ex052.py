núm = int(input('Digite um número: '))
cont = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m{}'.format(c), end=' ')
        cont += 1
    else:
        print('\033[31m{}'.format(c),end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
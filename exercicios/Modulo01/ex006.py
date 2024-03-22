num = int(input('Digite um número: '))
d = num * 2
t = num * 3
r = num ** (1 / 2)
print('O dobro de \033[1;4;32m{}\033[m é \033[1;4;33m{}\033[m, seu triplo é \033[1;4;33m{}\033[m. A sua raíz é \033[1;4;33m{:.2f}\033[m.'.format(num, d, t, r))

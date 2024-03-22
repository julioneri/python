import math
num = float(input('Digite um número: '))
#print ('O número inteiro de {} é {}'.format(num, round(num)))
#print('O Número inteiro de {} é {}'.format(num, math.trunc(num)))
print('O número inteiro de \033[4m{}\033[m é \033[4m{}\033[m'.format(num, int(num)))
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
me = (n1 + n2) / 2
cor = {'verde': '\033[1;32m',
       'amarelo': '\033[1;4;33m',
       'limpo': '\033[m'}
print('A média entre os números {}{:.1f}{} e {}{:.1f}{} é {}{:.1f}{}.'
      .format(cor['verde'], n1, cor['limpo'],
              cor['verde'], n2, cor['limpo'],
              cor['amarelo'], me, cor['limpo']))

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
#hi = (math.pow(co, 2) + (math.pow(ca, 2)))
#hi = (math.sqrt(sma))
#hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print ('O comprimento da hipotenusa é \033[33m{:.2f}\033[m'.format(hi))
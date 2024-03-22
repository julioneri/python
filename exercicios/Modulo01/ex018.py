from math import sin, cos, tan, radians
ângulo = float(input ('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de \033[31m{}\033[m tem:\nO Seno de \033[4;33m{:.2f}\033[m\nO Cosseno de \033[4;33m{:.2f}\033[m\nE a tangente de \033[4;33m{:.2f}\033[m'.format(ângulo, seno, cosseno, tangente))

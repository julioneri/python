d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi andado? '))
c1 = 60 * d
c2 = 0.15 * km
custo = c1 + c2
#print('O valor a pagar pelo aluguel do carro é: {}'.format(custo))
print('Valor por dias: \033[32mR${:.2f}\033[m'.format(c1))
print('Valor por km rodados: \033[32mR${:.2f}\033[m'.format(c2))
print('Valor \033[4mTOTAL\033[m a pagar: \033[4;32mR${:.2f}\033[m'.format(custo))
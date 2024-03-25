casa = float(input('Valor da casa: \033[32mR$\033[m'))
salário = float(input('Salário do comprador: \033[32mR$\033[m'))
anos = int(input('Em quantos anos pretende pagar? '))
prestação = casa / (anos * 12)
print('Para comprar uma casa de \033[32mR${:.2f}\033[m em \033[33m{}\033[m anos,'.format(casa, anos), end='')
print(' a prestação será de \033[4;32mR${:.2f}\033[m.'.format(prestação))
if prestação > salário * 30 / 100:
    print('Empréstimo \033[4;31mNEGADO!\033[m')
else:
    print('Empréstimo \033[4;32mACEITO!\033[m')
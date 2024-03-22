real = float(input('Digite a quantidade de dinheiro em real: R$'))
print('Você possui \033[1;4;32mR${:.2f}\033[m, sendo um total de \033[1;4;32mU${:.2f}\033[m.'.format(real, real / 5.61))
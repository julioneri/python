valor = float(input('Digite o salário atual: \033[32mR$\033[m'))
porcentagem = float(input('Digite a porcentagem: '))
porce = valor + (valor * porcentagem / 100)
print('Com {}% de aumento, seu salário passou de \033[32mR${:.2f}\033[m para \033[32mR${:.2f}\033[m.'.format(porcentagem, valor, porce))
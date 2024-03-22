valor = float(input('Digite o preço do produto: \033[32mR$\033[m'))
porcentagem = int(input('Digite a porcentagem do desconto: '))
novo = valor - (valor * porcentagem / 100)
print('Tendo {}% de desconto, o produto que antes custava \033[32mR${}\033[m passou a custar \033[32mR${:.2f}\033[m'.format(porcentagem, valor, novo))
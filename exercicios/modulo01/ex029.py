v = float(input('Qual a velocidade do veículo? ').strip())
if v > 80:
    m = (v - 80) * 7
    print('\n\033[4mVocê excedeu o limite de velocidade\033[m!')
    print('A multa a ser paga é de \033[31mR${:.2f}\033[m'.format(m))
print('Tenha um bom dia! Dirija com segurança!')
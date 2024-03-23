viagem = int(input('Digite a distância em quilometragens: '))
print('Você está prestes a começar uma viagem de \033[33m{}Km.\033[m'.format(viagem))
#preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
if viagem <= 200:
    preço = viagem * 0.50
else:
    preço = viagem * 0.45
print('E o preço da sua passagem é de \033[4;32mR${:.2f}\033[m'.format(preço))
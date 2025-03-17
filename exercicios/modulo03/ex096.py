def área(larg, comp):
    are = larg * comp
    print(f'A Área de um terreno de {larg}x{comp} é de {are}m²')


# Programa principal
print('-' * 23)
print(' Controle de Terrenos ')
print('-' * 23)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

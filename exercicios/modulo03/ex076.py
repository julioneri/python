lista = ('Lápis', 1.75, 'Borracha', 2.55,
         'Caderno', 10.90, 'Estojo', 7.50,
         'Lapizeira', 3.20, 'Caneta', 2.90,
         'Mochila', 20.00, 'Transferidor', 4.50,
         'Compasso', 9.99, 'Hidrocor', 5.70)
print('-' * 39)
print(f'{"LISTA DE PREÇOS":^39}')
print('-' * 39)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
print('-' * 39)
lista = []
while True:
    quest = ' '
    lista.append(int(input('Digite um valor: ')))
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quest == 'N':
        break
print('=' * 37)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÃO faz parte da lista!')

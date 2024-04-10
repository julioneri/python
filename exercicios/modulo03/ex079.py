números = []
while True:
    quest = ' '
    n = int(input('Digite um valor: '))
    if n not in números:
        print('Valor adicionado com sucesso...')
        números.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    while quest not in 'SN':
        quest = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if quest == 'N':
        break
print('=' * 37)
números.sort()
print(f'Você digitou os valores {números}')

temp = []
princ = []
mai = men = 0
while True:
    quest = ' '
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    while quest not in 'SsNn':
        quest = str(input('Quer continuar? [S/N] ')).strip()[0]
    if quest in 'Nn':
        break
print(f'O número de pessoas cadastradas foram {len(princ)}')
print(f'O maior peso foi de {mai}KG. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}KG. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
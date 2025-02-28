ficha = list()
while True:
    quest = ' '
    aluno = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([aluno, [nota1, nota2], média])
    while quest not in 'SsNn':
        quest = str(input('Quer continuar? [S/N] ')).strip()[0]
    if quest in 'Nn':
        break
print('=' * 25)
print(f'{"No.": <4}{"NOME": <10}{"MÉDIA": >11}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i: <4}{a[0].capitalize():<10}{a[2]: >11.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    elif opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0].capitalize()} são {ficha[opc][1]}')
print('Programa encerrado!')

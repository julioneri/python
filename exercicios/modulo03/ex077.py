lista = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'ESTUDAR', 'PRATICAR',
         'DEDICAÇÃO', 'FUTURO', 'CURSO', 'PROGRAMADOR', 'LINGUAGEM')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
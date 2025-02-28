matriz = []
linha = int(input('Quantas linhas? '))
coluna = int(input('Quantas colunas? '))
ce1 = int(linha / 2)
ce2 = int(coluna / 2)
print('  ', end='')
for p in range(0, coluna):
    print(f'  {p}', end='')
print()
for l in range(0, linha):
    for c in range(0, coluna):
        if c == 0:
            print(f'{l:>2}', end=' ')
        if l != ce1 and c != ce2 and l != c:
            print('[ ]', end='')
        elif l == ce1 or c == ce2 or l == c:
            print('[\033[1mX\033[m]', end='')
    print()

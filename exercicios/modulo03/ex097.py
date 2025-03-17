def escreva(txt):
    núm = len(txt)
    print('~=' * núm)
    print(f'{txt.upper(): ^{núm*2}}')
    print('~=' * núm)


escrever = str(input('Escreva: '))
escreva(escrever)
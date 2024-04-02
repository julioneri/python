while True:
    print('-' * 33)
    núm = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 33)
    if núm < 0:
        break
    for c in range(1, 11):
        print(f'{núm} x {c:2} = {núm*c}')
print('Programa encerrado. Volte sempre!')
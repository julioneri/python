frase = str(input('Digite a frase: ')).strip().upper()  # .replace(' ', '')
noo = ''.join(frase)
yee = noo[::-1]
print('O inverso de {} é {}.'.format(frase, yee))
if noo.replace(' ', '') == yee.replace(' ', ''):
    print('Essa frase É um PALÍNDROMO!')
else:
    print('Essa frase NÃO É um PALÍNDROMO!')

frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" é revelada {} vezes'.format(frase.count('a')))
print('A letra "A" é revelada pela primeira vez em {}'.format(frase.find('a')+1))
print('A letra "A" é revelada pela última vez em {}'.format(frase.rfind('a')+1))
print('-=-' * 9)
print(' Analisador de Triângulos')
print('-=-' * 9)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
print('Processando...')
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s1 + s2:
    print('Os seguimentos acima \033[32mPODEM FORMAR\033[m um triângulo.')
else:
    print('Os seguimentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo.')
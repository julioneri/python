s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos acima \033[4;32mPODEM FORMAR\033[m um triângulo!')
    if s1 == s2 == s3:
        print('O triângulo formado será um \033[33mEquilátero\033[m, pois \033[4mtodos os lados\033[m são iguais.')
    elif s1 != s2 != s3 != s1:
        print('O triângulo formado será um \033[33mEscaleno\033[m, pois \033[4mnenhum dos lados\033[m são iguais.')
    else:
        print('O triângulo formado será um \033[33mIsóceles\033[m, pois \033[4mhá somente dois lados\033[m iguais.')
else:
    print('Os seguimentos acima \033[4;31mNÃO PODEM\033[m formar um triângulo!')
from datetime import date
idade = int(input('\033[34mAno de nascimento:\033[m '))
idade = date.today().year - idade
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: \033[4;34mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[4;34mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[4;34mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[4;34mSÊNIOR\033[m')
else:
    print('Classificação: \033[4;34mMASTER\033[m')
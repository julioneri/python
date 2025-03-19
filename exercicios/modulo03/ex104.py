def leiaInt(i):
    while True:
        a = str(input(i))
        if a.isnumeric() == False:
            print('\033[31mErro! Digite um número inteiro válido\033[m')
        else:
            return a



# Programa principal
n = leiaInt('Leia um número: ')
print(f'Você acabou de digitar o número {n}')
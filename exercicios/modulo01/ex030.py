num = int(input('Digite um número: '))
resultado = num % 2
if resultado == 0:
    print(f'O número \033[32m{num}\033[m é \033[4mPAR\033[m')
else:
    print(f'O número \033[32m{num}\033[m é \033[4mÍMPAR\033[m')
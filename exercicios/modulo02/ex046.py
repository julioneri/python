from time import sleep
start = int(input('Digite "0" para começar a contagem! '))
if start == 0:
    print('Contagem regressiva iniciada!')
    for c in range(10, -1, -1):
        print(c, ' ', end='')
        sleep(1)
    print('\n\033[1;4;33m* -=-= FELIZ ANO NOVO! =-=- *\033[m')
else:
    print('Contagem cancelada!')
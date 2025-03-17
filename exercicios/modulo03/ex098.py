from time import sleep


def contagem(i, f, p):
    print('-=' * 15)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=False) #Flush praticamente inútil...
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=False)
            sleep(0.3)
            cont -= p
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 1, 2)
print('-=' * 23)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contagem(ini, fim, pas)


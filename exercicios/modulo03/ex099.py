from time import sleep
def maior(* núm):
    maior = 0
    print('-=' * 15)
    print('Analisando valores passados...')
    sleep(1.5)
    cont = 0
    for valor in núm:
        print(valor, end=' ')
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
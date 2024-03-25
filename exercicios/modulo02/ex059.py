from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos valores
    [ 5 ] sair do programa''')
    opção = int(input('>>> O que deseja fazer? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'A multiplicação dos valores {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior é {n2}.')
        elif n1 == n2:
            print('Os dois valores são iguais.')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-==-' * 7)
    sleep(2.5)
print('Volte em breve! ^_^')

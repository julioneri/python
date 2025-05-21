from ferramentas import data
#from ferramentas.data import * <<< Importa tudo >>>
from time import sleep


while True:
    data.título('MENU PRINCIPAL')
    print('\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2\033[m - \033[34mCadastrar nova pessoa\033[m')
    print('\033[33m3\033[m - \033[34mSair do sistema\033[m')
    print('–' * 37)
    try:
        opc = int(input('\033[33mSua opção:\033[m '))
    except ValueError:
        print(c[1], 'ERRO: Por favor, digite um número inteiro válido.', c[0])
    else:
        if opc > 3:
            print(c[1], 'ERRO: Digite uma opção válida!', c[0])
        else:
            if opc == 1:
                data.menu_cadastros()
            if opc == 2:
                data.menu_adicionar()
            if opc == 3:
                data.título('Saíndo do Sistema... Até logo!')
                break
    sleep(1.5)

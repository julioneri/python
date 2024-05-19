while True:
    text_header('Gestor de Clientes')
    print('1. Adicionar um novo cliente ao sistema.'
          '\n2. Listar todos os clientes cadastrados.'
          '\n3. Buscar um cliente pelo nome ou e-mail.'
          '\n4. Remover um cliente do sistema.'
          '\n5. Encerrar o programa')

    try:
        opcao = int(input('\033[33mSelecione uma das opções: \033[m'))
    except ValueError:
        print('\n\033[31mEntrada inválida. Por favor, tente novamente.\033[m')
        continue
    else:

        match opcao:
            case 1:
                text_header('Adicionar um novo cliente ao sistema')
                adicionar_cliente()
            case 2:
                text_header('Listar todos os clientes cadastrados')
            case 3:
                text_header('Buscar um cliente pelo nome ou e-mail')
            case 4:
                text_header('Remover um cliente do sistema')
            case 5:
                text_header('Encerrando o programa...')
                break
            case _:
                print(
                    '\n\033[31mOpção inválida. Por favor, tente novamente.\033[m\n')
                continue

"""
Desafio: Criando um Sistema de Gestão de Clientes

Crie um programa em JavaScript que simule um sistema de gestão de clientes para uma empresa. Cada cliente terá as seguintes propriedades:

1. Nome
2. E-mail
3. Telefone

O programa deve ser capaz de realizar as seguintes operações:

1. Adicionar um novo cliente ao sistema.
2. Listar todos os clientes cadastrados.
3. Buscar um cliente pelo nome ou e-mail.
4. Remover um cliente do sistema.
"""

lista_clientes = []


def text_header(txt='Insert Your Text Here'):  # Cria um cabeçalho com o texto inserido
    print('\n' + f' {txt} '.center(50, '='))
    return


def adicionar_cliente():
    nome_cliente = str(input('Digite o nome do cliente: ')).strip().title()
    email_cliente = str(input('Digite o E-mail para contado: ')).strip().lower()
    telefone_cliente = int(input('Digite o telefone para contato: '))

    cliente = {
        'nome': nome_cliente,
        'email': email_cliente,
        'telefone': telefone_cliente
        }

    lista_clientes.append(cliente.copy())

    print('\n\033[32mCliente registrado com sucesso!\033[m')
    return


def listar_clientes():
    for c, cliente in enumerate(lista_clientes):
        print(f'Nome: {cliente['nome']}')
        print(f'E-mail: {cliente['email']}')
        print(f'Telefone: {cliente['telefone']}')
        return


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

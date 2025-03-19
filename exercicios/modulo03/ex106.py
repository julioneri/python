from time import sleep
cores = ('\033[m',      # 0 - sem cores
         '\033[31m',    # 1 - vermelho
         '\033[32m',    # 2 - verde
         '\033[33m',    # 3 - amarelo
         '\033[34m',    # 4 - azul
         '\033[35m'     # 5 - roxo
         );


def função(txt):
    texto(f'Acessando o manual do comando \'{txt}\'', 4)
    sleep(2.5)
    print(cores[5], end='')
    help(txt)
    print(cores[0], end='')


def texto(txt, cor=0):
    """
    => A função desse código é formatar um texto, também podendo aplicar cores;
    :param txt: Texto a ser formatado;
    :param cor: Cor a ser ultilizada ('1, 2 ou 3');
    :return: Sem retorno.
    """
    s = len(txt) + 4
    print(cores[cor], end='')
    print('~' * s)
    print(f'{txt: ^{s}}')
    print('~' * s)
    print(cores[0], end='')


# Programa principal
while True:
    texto('SISTEMA DE AJUDA PyHelp', 3)
    busca = str(input('Função ou Biblioteca > ')).strip().lower()
    if busca == 'fim':
        break
    else:
        v = função(busca)
texto('ATÉ LOGO!', 1)

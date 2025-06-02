from random import randint


def play_game():
    '''
    \033[35m==>\033[36m Dentro do seu próprio programa, o usuário poderá importar e
    chamar a função para desfrutar de um joguinho de adivinhação de palavras.\033[m

    \033[35m=>\033[36m O programa inclui também um menu de START, podendo ser disparado
    quantas vezes o usuário preferir até que decida encerrar a atividade.\033[m

    \033[35m=>\033[36m O programa é limitado, contendo somente 12 objetos para cada tema,
    sendo estes Animais e Objetos.\033[m

    \033[35m=>\033[36m O programa não retorna nenhum valor.\033[m

    \033[35m--  Feito por ShokinhoLaint. Divirta-se!\033[m
    '''
    def título(txt):
        print(f'\033[33m{txt}\033[m')

    letras = []
    jogo = {'animal': ['cachorro', 'cavalo', 'macaco',
                       'girafa', 'elefante', 'ovelha',
                       'gaivota', 'galinha', 'tucano',
                       'baleia', 'baiacu', 'golfinho'],
            'objeto': ['caneta', 'borracha', 'livro',
                       'caderno', 'lapiseira', 'transferidor',
                       'tapete', 'aspirador', 'retrato',
                       'computador', 'teclado', 'headset']}

    print('\033[34mESCOLHA UM TEMA:\033[m')
    for num, obj in enumerate(jogo):
        print(f'\033[36m[{num+1}] = [{obj.capitalize()}]\033[m')

    # ANÁLISE DO TEMA (animal, objeto)
    while True:
        try:
            theme = int(input('\033[34mDigite: \033[m'))
        except (ValueError, TypeError):
            print('\033[31m Opção inválida! Tente novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31m O usuário interrompeu o programa. Tente novamente.\033[m')
        else:
            if 1 <= theme <= len(jogo):
                if theme == 1:
                    theme = 'animal'
                if theme == 2:
                    theme = 'objeto'
                break
            else:
                print('\033[31m Opção inválida! Tente novamente.\033[m')
    print('-' * 25)

    # FERRAMENTAS PARA USAR NO PRÓXIMO WHILE (INÍCIO DO JOGO)
    erros = []
    tterros = 0
    dica = True
    opc = randint(0, 11)
    palavra = jogo[theme][opc]

    # COMEÇO DEFINITIVO DO JOGO
    print(f'QUANTIDADE DE LETRAS: {len(palavra)}')
    while True:
        print('-' * 25)
        if tterros == 5:
            print('\033[31mFIM DE JOGO! VOCÊ PERDEU!\033[m')
            break
        letris = 0
        print('PALAVRA: ', end='')
        for letra in palavra:
            if not letra in letras:
                print('_', end=' ')
            else:
                print(f'{letra}'.upper(), end=' ')
                letris += 1
        print()
        if len(palavra) == letris:
            print('\033[32mFIM DE JOGO! PARABÉNS!\033[m')
            break

        # USUÁRIO ESCOLHE A LETRA PRO JOGO
        while tterros != 5:
            try:
                let = str(input('\033[34mDigite uma letra: \033[m')).strip().lower()[0]
            except IndexError:
                print('\033[31m Erro: Por favor, digite algo válido.\033[m')
            except KeyboardInterrupt:
                print('\033[31m O usuário interrompeu o programa. Tente novamente.\033[m')
            else:
                if let.isnumeric() or let.isalpha() == False:
                    if let == '*' and dica:
                        # DICA PRA ANIMAIS
                        if theme == 'animal':
                            if opc <= 5:
                                título('DICA: É UM ANIMAL TERRESTRE')
                            elif opc <= 8:
                                título('DICA: É UMA AVE')
                            else:
                                título('DICA: É UM ANIMAL AQUÁTICO')
                        # DICA PRA OBJETOS
                        elif theme == 'objeto':
                            if opc <= 5:
                                título('DICA: É UM OBJETO ESCOLAR')
                            elif opc <= 8:
                                título('DICA: É UM OBJETO DE SALA')
                            else:
                                título('DICA: É UM OBJETO DE QUARTO')
                        dica = False
                        break
                    elif let == '*' and dica == False:
                        título('Você já teve sua dica!')
                    else:
                        print('\033[31m Erro: Por favor, digite algo válido.\033[m')
                else:
                    print(f'LETRA DIGITADA: {let.upper()}')
                    if let in letras or let in erros:
                        print('\033[33m[!] Você já tentou essa letra.\033[m')
                        break

                    elif let not in palavra:
                        tterros += 1
                        erros.append(let)
                        print(f'\033[31m[!] NÃO há "{let.upper()}" na palavra.')
                        print(f'\tTOTAL DE ERROS: {tterros}\033[m')
                        break

                    elif let in palavra:
                        letras.append(let)
                        break
            print('-' * 25)
    print(f'\033[33mA PALAVRA ERA: {palavra}\033[m')

    # PLAYER INTERNO DA FUNÇÃO
    print('-' * 25)
    print('Deseja jogar novamente? [S/N] ')
    while True:
        try:
            start = str(input('Digite: ')).strip()[0]
        except (KeyboardInterrupt, IndexError):
            print('\033[31m Desculpe, não entendi!\033[m')
        else:
            if start in 'SsYy':
                print('-' * 25)
                play_game()
            elif start in 'Nn':
                print('Programa encerrado. Obrigado!')
                break
            else:
                print('\033[31mDesculpa, não entendi!\033[m')


play_game()
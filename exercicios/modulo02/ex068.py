from random import randint
vitórias = 0
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você escolheu {jogador} e o computador {computador}. Sendo um total de {total}:')
    print('PAR!' if total % 2 == 0 else 'ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitórias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitórias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitórias} vezes.')
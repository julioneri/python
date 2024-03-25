from random import randint
computador = randint(0, 10)
print('Olá, eu sou o seu computador! Irei pensar em um número entre 0 e 10.')
print('Você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    número = int(input('Qual é o seu palpite? '))
    palpites += 1
    if número == computador:
        acertou = True
    else:
        if número < computador:
            print('Mais... Tente novamente.')
        elif número > computador:
            print('Menos... Tente mais uma vez.')
print(f'Você acertou com {palpites} tentativas.')

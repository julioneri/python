from random import choice
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)
print('\033[35m-=-\033[m' * 13)
print('\033[34m         VAMOS JOGAR JOKENPO!\033[m')
print('\033[35m-=-\033[m' * 13)
user = str(input('Escolha entre pedra, papel e tesoura: ')).strip().upper()
print('JO ', end='')
sleep(1)
print('KEN ', end='')
sleep(1)
print('PO!!!')
sleep(1)
if user == computador:
    print('Vocês escolheram a mesma coisa!'.format(user))
if user == 'PEDRA' and computador == 'PAPEL':
    print('\033[4;31mVocê perdeu!\033[m')
if user == 'PAPEL' and computador == 'TESOURA':
    print('\033[4;31mVocê perdeu!\033[m')
if user == 'TESOURA' and computador == 'PEDRA':
    print('\033[4;31mVocê perdeu!\033[m')

if user == 'PEDRA' and computador == 'TESOURA':
    print('\033[4;32mVocê ganhou!\033[m')
if user == 'PAPEL' and computador == 'PEDRA':
    print('\033[4;32mVocê ganhou!\033[m')
if user == 'TESOURA' and computador == 'PAPEL':
    print('\033[4;32mVocê ganhou!\033[m')

print(f'O computador escolheu \033[4;33m{computador}\033[m')
from random import randint
from time import sleep
computador = randint(1, 5) # Faz o computador "PENSAR"
print('\033[35m-=-\033[m' * 19)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[35m-=-\033[m' * 19)
jogador = int(input('Em que número estou pensando? ')) # Jogador tenta adivinhar
print('Processando...')
sleep(1)
if jogador <= 5:
    print('\033[4;32mVocê Acertou!\033[m' if jogador == computador else '\033[4;31mVocê errou!\033[m')
else:
    print('\033[31mO número que você escolheu é maior que 5.\033[m')
print(f'Eu pensei em \033[4m{computador}\033[m!')
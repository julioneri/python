lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezeito', 'dezenove', 'vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        print(f'Você digitou o número {lista[núm]}')
        opção = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        while opção not in 'SN':
            opção = str(input('Não entendi. Deseja continuar? [S/N] ')).strip().upper()[0]
        if opção == 'N':
            break
    else:
        print('Tente novamente. ', end='\n')
print('Programa encerrado! Até breve!')

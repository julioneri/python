opção = 'S'
soma = cont = maior = menor = 0
while opção in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    cont += 1
    if cont == 1:
        maior = menor = núm
    elif núm > maior:
        maior = núm
    elif núm < menor:
        menor = núm
    opção = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
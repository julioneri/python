maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o {c}° peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{}Kg foi o maior e {}Kg foi o menor peso.'.format(maior, menor))
núm = cont = soma = 0
while núm != 999:
    núm = int(input('Digite um número: '))
    if núm != 999:
        cont += 1
        soma += núm
print(f'{cont} números foram digitados.'
      f'\nA soma entre eles é {soma}')

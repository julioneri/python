count = soma = 0
while True:
    núm = int(input('Digite um número (999 para parar): '))
    if núm == 999:
        break
    count += 1
    soma += núm
print(f'A soma dos {count} valores foi {soma}!')

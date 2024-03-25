soma = 0
count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        count += 1
        soma += c
print('A soma entre todos os {} valores solicitados é {}'.format(count, soma))
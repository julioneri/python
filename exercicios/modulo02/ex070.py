total = totmil = menor = 0
barato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        totmil += 1
    if menor == 0 or preço < menor:
        menor = preço
        barato = nome
    opção = ' '
    while opção not in 'SN':
        opção = input('Quer continuar? [S/N] ').strip().upper()[0]
    if opção == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')

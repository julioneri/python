print('======= BANCO SHOKEY =======')
valor = int(input('Que valor você quer sacar? R$'))
notas50 = valor // 50
resto50 = valor % 50
notas20 = resto50 // 20
resto20 = resto50 % 20
notas10 = resto20 // 10
resto10 = resto20 % 10
if notas50 != 0:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 != 0:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 != 0:
    print(f'Total de {notas10} cédulas de R$10')
if resto10 != 0:
    print(f'Total de {resto10} cédulas de R$1')
print('=' * 29)
print('Volte sempre!')
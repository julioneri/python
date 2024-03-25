from datetime import date
noo = 0
yee = 0
for c in range(1, 7+1):
    data = int(input(f'Data de nascimento da {c}ª pessoa: '))
    if data + 21 > date.today().year:
        noo += 1
    if data + 21 <= date.today().year:
        yee += 1
print(f'{noo} pessoas ainda não atingiram a maioridade e {yee} já atingiram a maioridade.')
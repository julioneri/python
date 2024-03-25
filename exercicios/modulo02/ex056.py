media = 0
idadevelho = 0
nomevelho = ''
mulheres20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1
médiaidade = media / 4
print(f'A média de idade do grupo é {médiaidade} anos')
print(f'O homem mais velho tem {idadevelho} anos e se chama {nomevelho}')
print(f'Ao todo há {mulheres20} mulher(es) com menos de 20 anos')
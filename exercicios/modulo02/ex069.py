homens = pess18 = mulh18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        pess18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulh18 += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {pess18}
Ao todo temos {homens} homens cadastrados
E temos {mulh18} mulheres com menos de 20 anos''')

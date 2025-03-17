lista = []
dados = {}
média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).capitalize()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    média += dados['idade']
    lista.append(dados.copy())
    while True:
        opc = str(input('Quer continuar? [S/N] ')).strip()[0]
        if opc in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if opc in 'Nn':
        break
print('-=' * 30)
print(f'A) Ao todo tempos {len(lista)} pessoas cadastradas.')
média = média / len(lista)
print(f'B) A média de idade é de {int(média)} anos.')
print('C) As mulheres cadastradas foram ', end='')
for c in lista:
    if c['sexo'] in 'Ff':
        print(f'[{c["nome"]}]', end=' ')
print('\nD) Lista de pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<< ENCERRADO >>>')

time = []
gols = []
geral = {}

while True:
    geral.clear()
    print('-' * 30)
    geral['nome'] = str(input('Nome do jogador: '))
    geral['partidas'] = int(input(f'Quantas partidas {geral["nome"]} jogou? '))
    for p in range(1, geral['partidas']+1):
        gols.append(int(input(f'Quantos gols na partida {p}? ')))
    geral['gols'] = gols[:]
    time.append(geral.copy())
    gols.clear()
    while True:
        quest = str(input('Quer continuar? [S/N] ')).strip()[0]
        if quest in 'SsNn':
            break
        print('ERRO! Responda apenas com S ou N.')
    if quest in 'Nn':
        break
print('-=' * 30)
print(f'{"Cód.": >5} {"Nome": <11}{"Gols": <21}{"Total"}')
print('-' * 47)
for i, c in enumerate(time):
    total = 0
    for t in c["gols"]:
        total += t
    print(f' {i: <5}{c["nome"]: <11}{str(c["gols"]):<21}{total}')
while True:
    print('-' * 47)
    dados = int(input('Mostrar dados de qual jogador? '))
    if dados == 999:
        break
    elif dados < len(time):
        print(f'-- LEVANTAMENTO DE DADOS DO JOGADOR {time[dados]["nome"].capitalize()}:')
        for i, g in enumerate(time[dados]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente.')
print('<<< VOLTE SEMPRE! >>>')

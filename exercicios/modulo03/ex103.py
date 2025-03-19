def ficha(nome, gols):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.isnumeric() == False:
        gols = 0
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
ficha(nome, gols)

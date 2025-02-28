lista = []
dic = {}
dic['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
quantp = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for c in range(0, quantp):
    lista.append(int(input(f'Quantos gols na {c+1}ª partida? ')))
dic['gols'] = lista[:]
dic['total'] = sum(lista)
print('-=' * 30)
print(dic)
print('-=' * 30)
for k in dic:
    print(f'O campo {k} tem o valor {dic[k]}.')
print('-=' * 30)
print(f'O {dic["nome"]} jogou {len(dic["gols"])} partidas.')
for i, c in enumerate(dic['gols']):
    print(f'   => Na partida {i+1}, fez {c} gols.')
print(f'Foi um total de {dic["total"]} gols.')

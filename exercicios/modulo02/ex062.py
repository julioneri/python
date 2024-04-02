termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
cont = 1
mais = 10
quantidade = 0
while mais != 0:
    quantidade += mais
    while cont <= quantidade:
        print(termo, end=' > ')
        termo = termo + razão
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais pretende ver? '))
print(f'Programa encerrado com um total de {quantidade} termos mostrados.')
print('FIM')
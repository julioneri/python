lista = ('ATLÉTICO-MG', 'FLAMENGO', 'PALMEIRAS', 'FORTALEZA', 'CORINTHIANS',
         'BRAGANTINO', 'FLUMINENSE', 'AMÉRICA-MG', 'ATLÉTICO-GO', 'SANTOS',
         'CEARÁ', 'INTERNACIONAL', 'SÃO PAULO', 'ATHLETICO-PR', 'CUIABÁ',
         'JUVENTUDE', 'GRÊMIO', 'BAHIA', 'SPORT', 'CHAPECOENSE')
print(f'Lista de times do Brasileirão: {lista}')
print('=-' * 17)
print(f'Os cinco primeiros são {lista[0:5]}')
print('=-' * 17)
print(f'Os quatro últimos são {lista[-4:]}')
print('=-' * 17)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('=-' * 17)
print(f'A chapecoense está na {lista.index("CHAPECOENSE") + 1}ª posição.')

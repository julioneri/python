cidade = input('Digite o nome da sua cidade: ').strip()
print('Sua cidade possui "Santo" no começo?\033[32m', cidade[:5].capitalize() == 'Santo')
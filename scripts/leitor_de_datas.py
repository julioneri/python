from datetime import date
ano_atual = date.today().year

def leiaAno(txt):
    while True:
        try:
            i = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Tente novamente.\033[m')
        else:
            if 0 < i <= ano_atual:
                return i
            else:
                print('\033[31m ERRO: Tente novamente.\033[m')


def leiaMes(txt):
    while True:
        try:
            m = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Tente novamente.\033[m')
        else:
            if 0 < m <= 12:
                return m
            else:
                print('\033[31m ERRO: Tente novamente.\033[m')


def leiaDia(txt):
    while True:
        try:
            d = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31m ERRO: Tente novamente.\033[m')
        else:
            if 0 < d <= 31:
                return d
            else:
                print('\033[31m ERRO: Tente novamente.\033[m')


ano = leiaAno('Ano de nascimento: ')
mes = leiaMes('Mês de nascimento: ')
dia = leiaDia('Dia de nascimento: ')
meses = ['janeiro', 'fevereiro', 'março', 'abril',
         'maio', 'junho', 'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro']

print(f'Você nasceu em {dia} de {meses[mes-1]} de {ano}')
idade = ano_atual - ano
print(f'Em {ano_atual} você fará {idade} anos')
resta = mes - date.today().month
print(f'Faltam {resta} mêses pro seu aniversário.')

mes_atual = date.today().month
if mes_atual < mes:
    print('Você ainda não fez aniversário este ano.')
elif mes_atual > mes:
    print('Você já fez aniversário este ano.')
else:
    print('Estamos no mês do seu aniversário.')


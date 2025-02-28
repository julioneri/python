from datetime import datetime
dic = {}
dic['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de Nascimento: '))
dic['idade'] = datetime.now().year - nasc
dic['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dic['ctps'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salário'] = float(input('Salário: R$ '))
    dic['aposentadoria'] = dic['idade'] + (dic['contratação'] + 35 - datetime.now().year)
print('-=' * 30)
for e in dic:
    print(f'{e} tem valor {dic[e]}')

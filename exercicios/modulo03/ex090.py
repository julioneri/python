aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
#print(aluno.items()) MOSTRA CHAVES E VALORES
#print(aluno.values()) MOSTRA SOMENTE OS VALORES
#print(aluno.keys()) MOSTRA SOMENTE AS CHAVES
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
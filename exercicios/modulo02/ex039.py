from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
print('Qual o seu sexo?'
      '\n\033[33m[ A ] MASCULINO'
      '\n[ B ] FEMININO\033[m')
sexo = str(input('Digite: ')).strip().upper()
if sexo == 'B':
    print('Você não precisa fazer o alistamente militar obrigatório!')
idade = atual - nasc
if sexo == 'A':
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if sexo != 'A' and sexo != 'B':
    print('Não reconhecido. Tente novamente!')
if idade > 18 and sexo == 'A':
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamente foi em {}.'.format(nasc + 18))
elif idade < 18 and sexo == 'A':
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamente será em {}'.format(nasc + 18))
elif idade == 18 and sexo == 'A':
    print('Você deve se alistar IMEDIATAMENTE!')
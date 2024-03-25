nota1 = float(input('Primeira média: '))
nota2 = float(input('Segunda média: '))
media = (nota1 + nota2) / 2
print('Com {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('\033[31mVocê foi reprovado!\033[m')
elif 5 <= media < 7:
    print('\033[33mVocê ficou em recuperação.\033[m')
elif media >= 7:
    print('\033[32mParabéns! Você foi aprovado!\033[m')
print('A sua média é \033[4m{:.1f}\033[m.'.format(media))

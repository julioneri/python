def voto(idade):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO NÃO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# Programa principal
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

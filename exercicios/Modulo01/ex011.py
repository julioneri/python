lar = float(input('Qual a \033[31mlargura\033[m da parede? '))
alt = float(input('Qual a \033[31maltura\033[m da parede? '))
are = lar * alt
tin = are / 2
print(f'Sua parede tem a \033[4mdimensão\033[m de {lar}x{alt}'
      f' e sua \033[4márea\033[m é de {are}m².'
      f'\nPara pintar, você precisará de \033[4;33m{tin}l\033[m de tinta.')
def notas(* notes, situ=False):
    """
    => Função para analisar notas e situações de vários alunos.
    :param notes: Uma ou mais notas dos alunos (aceita várias)
    :param situação: valor opicional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dic = dict()
    dic['total'] = len(notes)
    dic['maior'] = max(notes)
    dic['menor'] = min(notes)
    dic['média'] = sum(notes)/len(notes)
    if situ:
        if dic['média'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['média'] >= 5:
            dic['situação'] = 'RAZOÁVEL'
        else:
            dic['situação'] =  'RUIM'
    return dic


#Programa principal
buscar = notas(7, 5, 8, 6, 9, situ=True)
print(buscar)
#help(notas)

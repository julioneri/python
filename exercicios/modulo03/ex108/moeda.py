def metade(preço=0):
    r = preço / 2
    return r


def dobro(preço=0):
    r = preço * 2
    return r


def aumentar(preço=0, taxa=0):
    r = preço + (preço * taxa / 100)
    return r


def diminuir(preço=0, taxa=0):
    r = preço - (preço * taxa / 100)
    return r

def moeda(preço):
    r = f'R${preço:.2f}'.replace('.', ',')
    return r



def factorial(n, show=False):
    """
    => Calcula o Fatorial de um número.
    :param n: O Número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O Valor do Fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


# Programa principal
print(factorial(5, show=True))
#help(factorial)

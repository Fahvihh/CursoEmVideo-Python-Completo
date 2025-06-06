def fatorial(n, Show=False):
    """
    -> Calculo de fatorial
    :param Num: Número a ser calculado.
    :param Show: Opcional (se deseja ou não mostrar a conta).
    :return: O valor fatorial de Num.
    -> Criado por Fatima para resolução do exerício.
    """
    f = 1
    for c in range(n,0,-1):
        if Show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)
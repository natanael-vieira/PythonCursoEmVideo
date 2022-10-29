print('===== CÁCLULO FATORIAL DE UM NÚMERO QUALQUER =====\n')


def fatorial(n, show=False):
    """
    => Calcula o Fatorial de um número qualquer.
    :param n: O número que será calculado
    :param show: (opcional) mostrar ou não a conta sendo realizada.
    :return: O valor do fatorial n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
n = int(input('Digite um número para ser calulado: '))
fatorial(n)
print(fatorial(n, show=True))
help(fatorial)

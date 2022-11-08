def aumentar(preco):
    preco = preco + ((preco * 17) / 100)
    return preco


def diminuir(preco):
    preco = preco - ((preco * 11) / 100)
    return preco


def dobro(preco):
    return preco * 2


def metade(preco):
    return preco / 2


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')
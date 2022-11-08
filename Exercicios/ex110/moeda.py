def aumentar(preco = 0, taxa = 0, formato = False):
    '''
    ==> Função para calcular o aumento de um determinado preço e
    que retorna o resultado com ou sem formatação.
    :param preco: o preco que se quer aumentar
    :param taxa: o percentual que se quer aplicar em cima do preco
    :param formato: para formatar o resultado em tela ou não
    :return: o valor reajustado retorna
    '''
    res = preco + ((preco * taxa) / 100)
    return preco if not formato else moeda(res)
    

def diminuir(preco = 0, taxa = 0, formato = False):
    res = preco - ((preco * taxa) / 100)
    return preco if not formato else moeda(res)


def dobro(preco = 0, formato = False):
    res =  preco * 2
    return res if not formato else moeda(res)


def metade(preco = 0, formato = False):
    res =  preco / 2
    return res if not formato else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')


def resumo(preco = 0, taxaa = 17, taxar = 11):
    print('='*43)
    print('RESUMO DO VALOR'.center(43))
    print('='*43)
    print(f'VALOR INICIAL DIGITADO: \t{moeda(preco)}')
    print(f'DOBRO DO VALOR INICIAL: \t{dobro(preco, True)}')
    print(f'METADE DO VALOR INICIAL: \t{metade(preco, True)}')
    print(f'AUMENTA {taxaa}% NO VALOR INICIAL: \t{aumentar(preco, taxaa, True)}')
    print(f'DESCONTA {taxar}% NO VALOR INICIAL: \t{diminuir(preco, taxar, True)}')
    print('='*43)

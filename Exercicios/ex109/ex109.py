import moeda

preco = float(input('Digite o preço do produto: R$ '))

print(f'\nA METADE de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O DOBRO do {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Com ACRÉCIMO de 17% fica {moeda.aumentar(preco, 17, True)}')
print(f'Com DESCONTO de 11% fica {moeda.diminuir(preco, 11, True)}')

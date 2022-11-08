import moeda

preco = float(input('Digite o preço do produto: R$ '))

print(f'\nA METADE de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O DOBRO do {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Com ACRÉCIMO de 17% fica {moeda.moeda(moeda.aumentar(preco))}')
print(f'Com DESCONTO de 11% fica {moeda.moeda(moeda.diminuir(preco))}')

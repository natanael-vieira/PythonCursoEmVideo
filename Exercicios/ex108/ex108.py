import moeda

preco = float(input('Digite o preço do produto: R$ '))

print(f'\nA METADE de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O DOBRO do {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'O preço {moeda.moeda(preco)} com ACRÉCIMO de 17% é {moeda.moeda(moeda.aumentar(preco))}')
print(f'O preço {moeda.moeda(preco)} com DESCONTO de 11% é {moeda.moeda(moeda.diminuir(preco))}')

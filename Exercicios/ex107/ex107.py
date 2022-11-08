import moeda

preco = float(input('Digite o preço do produto: R$ '))

print(f'\nA METADE de {preco} é {moeda.metade(preco)}')
print(f'O DOBRO do {preco} é {moeda.dobro(preco)}')
print(f'O preço {preco} com ACRÉCIMO de 17% é {moeda.aumentar(preco)}')
print(f'O preço {preco} com DESCONTO de 11% é {moeda.diminuir(preco)}')

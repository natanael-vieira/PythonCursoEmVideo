import moeda

preco = float(input('Digite o preço do produto: R$ '))

print(f'\nA METADE do preço digitado é R$ {moeda.metade(preco):.2f}')
print(f'O DOBRO do preço digitado é R$ {moeda.dobro(preco):.2f}')
print(f'O preço com ACRÉCIMO de 17% é R$ {moeda.aumentar(preco):.2f}')
print(f'O preço com DESCONTO de 11% é R$ {moeda.diminuir(preco):.2f}')

import math
import random
import emoji

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é igual a {raiz:.2f}')

n = random.randint(0, 400)
square = math.sqrt(n)

print(f'A raiz de {n} é {square:.3f}.')

print(emoji.emojize('E é assim que se faz raiz quadrada em Python :sunglasses: !'))
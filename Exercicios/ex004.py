import string
from unicodedata import numeric


print('Vamos criar um script onde o que for digitado mostre em tela o seu tipo primitivo e todas as informações possíveis sobre ela')

algo = input('Digite algo: \n')

print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minúsuculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle())

print('\nMétodo de print abaixo usando o FORMAT (f) e as chaves:\n')

print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsuculas? {algo.islower()}')
print(f'Está capitalizada? {algo.istitle()}')

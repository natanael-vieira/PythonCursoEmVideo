import random

a = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

print(f'O números sorteados foram: ', end='')

for n in a:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi: {max(a)}')
print(f'O menor valor sorteado foi: {min(a)}')

print('===== MATRIZ 3X3 =====\n')

num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um número: '))

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}]', end='')
        if num[l][c] % 2 == 0:
            somap += num[l][c]    
    print()

print()

for c in range(0, 3):
    if c == 0:
        maior = num[1][c]
    elif num[1][c] > maior:
        maior = num[1][c]

terceira = num[0][2] + num[1][2] + num[2][2]

print(f'A SOMA dos valores PARES é: {somap}')
print(f'A SOMA dos valores da TERCEIRA COLUNA é: {terceira}')
print(f'o MAIOR valor da segunda linha é: {maior}')

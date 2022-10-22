print('===== MATRIZ 3X3 =====\n')

num = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        num[l][c] = int(input(f'Digite um número: '))

print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{num[l][c]:^5}]', end='')
    print()
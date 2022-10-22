print('===== NÚMEROS PARES E ÍMPARES CRESCENTE =====\n')

num = [[],[]]
v = 0

for i in range(1, 8):
    v = int(input('Digite um número: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)

num[0].sort()
num[1].sort()

print(f'\nOs números PARES digitados foram: {num[0]}')
print(f'Os números ÍMPARES digitados foram: {num[1]}\n')

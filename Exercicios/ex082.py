print('===== VÁRIOS NÚMEROS E PAR OU ÍMPAR =====\n')

list = []
pares = []
impares = []

while True:
    list.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

print(f'\nA lista completa dos números digitados é: {list}')

for i, v in enumerate(list):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Os números PARES digitados foram: {pares}')
print(f'Os números ÍMPARES digitados foram: {impares}')

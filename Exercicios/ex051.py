print('===== PROGRESSÃO ARITMÉTICA =====\n')

n = int(input('Digite o termo: '))
r = int(input('\nDigite a razão: '))
dez = n + (10 - 1) * r

for c in range(n, dez + r, r):
    print(c)

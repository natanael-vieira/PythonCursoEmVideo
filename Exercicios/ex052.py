print('===== NÚMEROS PRIMOS =====')

n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        t = t + 1
if t == 2:
    print(f'O número {n} é um número primo!')
else:
    print(f'O número {n} não é um número primo!')

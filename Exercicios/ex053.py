print('===== PALÍNDROMO =====\n')

f = str(input('Digite uma palavra ou uma frase: ')).replace(' ', '').strip().upper()
cf = ''

for n in range(len(f) -1, -1, -1):
    cf += f[n]
if cf == f:
    print('Temos um palíndromo!')
else:
    print('A palavra/frase digitada não é um palíndromo')

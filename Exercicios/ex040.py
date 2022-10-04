print('===== VERIFIQUE APROVADO OU REPROVADO =====\n')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('\nDigite sua segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print(f'Sua média foi: {m:.2f}. REPROVADO!')
elif m >= 5.0 and m <= 6.99:
    print(f'Sua média foi: {m}. RECUPERAÇÃO!')
else:
    print(f'Sua média foi: {m}. APROVADO')

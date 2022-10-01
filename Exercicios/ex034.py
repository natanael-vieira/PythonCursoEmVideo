sal = float(input('Digite o valor do salário do funcionário: '))

if sal > 1250.00:
    aum = sal + (sal*10/100)
    print(f'O salário R${sal:.2f} teve um acréscimo de 10% e passou a ser R${aum:.2f}')
else:
    aum2 = sal + (sal*15/100)
    print(f'O salário R${sal:.2f} teve um acréscimo de 15% e passou a ser R${aum2:.2f}')


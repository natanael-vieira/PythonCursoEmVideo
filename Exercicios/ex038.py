print('===== COMPARANDO NÚMEROS =====\n')

pri = int(input('Digite o primeiro número: \n'))
seg = int(input('Digite o segundo número: \n'))

if pri > seg:
    print(f'O primeiro valor {pri} é MAIOR que o segundo {seg}!')
elif seg > pri:
    print(f'O segundo valor {seg} é MAIOR que o primeiro {pri}!')
else:
    print('Os dois números são iguais!')

print('===== BANCO BAMERINDUS =====\n')
print('O CAIXA possui as cédulas de R$ 50.00 de R$ 20.00 de R$ 10.00 e de R$ 1.00')
valor = int(input('Informe o valor a ser SACADO: R$ '))
total = valor
ced = 50
contCed = 0

while True:
    if total >= ced:
        total -= ced
        contCed += 1
    else:
        if contCed > 0:
            print(f'Total de {contCed} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contCed = 0
        if total == 0:
            break

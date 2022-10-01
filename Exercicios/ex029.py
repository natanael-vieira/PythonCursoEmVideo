print('===== VERIFIQUE O VALOR DE SUA MULTA =====\n')
vel = int(input('Insira a velocidade: '))
mult = float((vel - 80) * 7)

if vel > 80:
    print('Você foi multado!')
    print(f'Você passou à {vel}Km/h. O valor da sua multa é: R${mult:.2f}!\n')
else:
    print('Muito bem, sempre siga as leis de trânsito!\n')

print('===== CÁLCULO DE IMC =====\n')

p = float(input('Digite seu peso: '))
a = float(input('\nDigite sua altura: '))

imc = float(p / (a * a))

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}, então você está ABAIXO DO PESO.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}, então você está no PESO IDEAL.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f}, então você está com SOBREPESO.')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f}, então você está OBESO.')
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f}, então você está com OBESIDADE MÓRBIDA.')

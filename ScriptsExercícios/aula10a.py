time = int(input('Quantos anos tem seu carro? '))

if time <= 5:
    print('Seu carro é novo!')
else:
    print('Seu carro é clássico!')

print('=== FIM ===')

# Ou simplificando o código fica dessa forma

tempo = int(input("Quantos anos tem seu carro? "))
print('Seu carro é novo!' if tempo <= 5 else 'Seu carro é clássico')
print('=== É ISSO ===')

name = str(input('\nQual é seu nome? '))
if name == 'Abigail':
    print('Que nome lindo você tem!')

print(f'Bom dia, {name}!')


nome = str(input('\nQual seu nome? '))
if nome == 'Abigail':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')


n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
m = (n1 + n2) / 2
print(f'\nSua média é: {m:.2f}')

if m >= 8.0:
    print('Parabéns!')
elif m >= 6.0:
    print('Muito Bom!')
elif m < 6.0:
    print('Acelera!')
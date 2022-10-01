km = int(input('Digite a distância a ser percorrida em viagem, em Km: '))

if km <= 200:
    v1 = km * 0.50
    print(f'Sua viagem de {km}Km custará: R${v1:.2f}!')
else:
    v2 = km * 0.45
    print(f'Sua viagem de {km}Km custará: R${v2:.2f}')

print('Boa Viagem!')
print('=' * 35)
print('     MEDINDO ÁREA DE TERRENOS        ')
print('=' * 35)
print()

def area(l, c):
    print()
    res = l * c
    print(f'A área do terreno informado é de {res:.2f}m².')


largura = float(input('Largura do terreno [m]: '))
comprimento = float(input('Comprimento do terreno [m]: '))

area(largura, comprimento)

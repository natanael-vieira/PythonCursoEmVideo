import math

co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
hi = (co**2) + (ca**2)
hipo = math.sqrt(hi)

print(f'A hipotenusa do cateto oposto {co} e do cateto adjacente {ca} é {hipo}.')

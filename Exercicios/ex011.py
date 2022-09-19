larg = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = larg * alt
tint = area / 2

print(f'A quantidade de tinta necessária para pintar {area:.2f}m², que é a área da sua parede, é de {tint:.1f} litros de tinta.')
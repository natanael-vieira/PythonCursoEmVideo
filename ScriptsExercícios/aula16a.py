rango = ('Arroz', 'Feijão', 'Bife', 'Batata Frita', 'Refrigerante')

for cont in range(0, len(rango)):
    print(f'Eu vou comer no almoço: {rango[cont]} na posição {cont}')

print('\nO almoço estava demais!\n')

for c in rango:
    print(f'Eu vou comer no almoço: {c}')

print('\nO almoço estava demais!')

for pos, comida in enumerate (rango):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\nO almoço estava demais!\n')

print(sorted(rango)) #Aqui o sorted vai ordenar a tupla em ordem alfabética/numérica, além de criar uma lista com ela

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(c)
print(c.count(5)) #.count mostra quantas vezes o número dentro dos parênteses aparece na tupla
print(c.index(5)) 

# val = []
# print(val)

# val.append(5)
# val.append(9)
# val.append(4)
# print(val)

# for v in val:
#     print(f'Os valores cadastrados foram {v}')

# for p, c in enumerate(val):
#     print(f'Na posição {p} eu encontrei o valor {c}')
# print('Cheguei ao final da lista.')

# valores = []
# print(valores)

# for cont in range(0, 5):
#     valores.append(int(input('Digite um número: ')))
# print(valores)

# for v in valores:
#     print(f'Os valores cadastrados foram {v}')

# for p, c in enumerate(valores):
#     print(f'Na posição {p} eu encontrei o valor {c}')
# print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a # Desta forma estou fazendo apenas uma ligação entre as duas listas, isto é uma peculiaridade de Python, quando atribuo uma lista a uma outra eles se torna ligadas entre si, se alterar uma a outra também sofre a alteração
print(f'A Lista A: {a}')
print(f'A Lista B: {b}')

b[2] = 8
print(f'\nA Lista A: {a}')
print(f'A Lista B: {b}')

b = a[:] # Quando uso o [:] em qualquer lista, eu não estou fazendo uma ligação, mas sim uma cópia
b[2] = 1

print(f'\nA Lista A: {a}')
print(f'A Lista B: {b}')
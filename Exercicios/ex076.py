lista = ('Arroz', 9.99, 'Feijão', 8.99, 'Macarrão', 3.99, 'Sardinha', 5.99, 'Miojo', 1.99, 'Café', 14.90, 'Iogurte', 4.79, 'Margarina', 12.90, 'Pão', 14.50, 'Carne', 35.99, 'Frango', 19.90)

print('='*40)
print(f'{"LISTA DE COMPRAS":^40}')
print('='*40)

for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f' R${lista[item]:>7.2f}')
print('='*40)

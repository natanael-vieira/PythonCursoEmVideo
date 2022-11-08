from uteis import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)

print(f'\nO FATORIAL de {num} é {fat}.')
print(f'O DOBRO de {num} é {numeros.dobro(num)}.')
print(f'O TRIPLO de {num} é {numeros.triplo(num)}.')

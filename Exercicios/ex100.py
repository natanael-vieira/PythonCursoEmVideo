from random import randint
from time import sleep

print('===== SOMA NÚMEROS PARES =====\n')

def sorteia(list):
    print('Sorteando os 5 valores da lista...')
    sleep(1)
    for cont in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(list):
    sleep(1)
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'Os valores pares da lista {list}, somando apenas os pares temos o resultado: {soma}')
    print()


#Programa Principal
num = []
sorteia(num)
somaPar(num)

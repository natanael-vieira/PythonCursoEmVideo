import math
from random import randint
from time import sleep

print('===== MEGA DA VIRADA =====\n')

list = []
jogos = []
quant = int(input('Quantos jogos quer fazer? '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num  = randint(1, 60)
        if num not in list:
            list.append(num)
            cont += 1
        if cont >= 6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    total +=1

print('\n=====', f'SORTEANDO {quant} JOGOS', '=====')

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

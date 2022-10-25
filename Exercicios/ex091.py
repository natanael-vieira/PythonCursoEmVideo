from pickletools import read_int4
from random import randint
from time import sleep
from operator import itemgetter

print('===== JOGO DE DADOS =====\n')

jogo = {'jogador1': randint(1, 6), 
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1,6)
}

ranking = {}

print('Os números sorteados foram: ')

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
    
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('\nColocação dos jogadores:\n')

for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')

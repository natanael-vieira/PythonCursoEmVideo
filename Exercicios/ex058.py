import random
print('Será que você consegue advinhar o número que escolhi?\n')
npc = -1
num = 0
jog = 1

while num != npc:
    num = int(input('Escolha um número inteiro entre 0 e 10: '))
    npc = random.randint(0,10)
    if num != npc:
        print('Você errou, Tente novamente!')
        jog += 1

print(f'Você GANHOU e precisou de {jog} jogadas!')
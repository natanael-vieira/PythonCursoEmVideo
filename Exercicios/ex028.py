import random
print('Será que você consegue advinhar o número que escolhi?\n')
npc = random.randint(0,5)
num = int(input('Escolha um número inteiro entre 0 e 5: '))

if num == npc:
    print(f'O numero escolhido por mim foi {npc}. Parabéns, você acertou!')
else: 
    print(f'Tente novamente, o número que escolhi foi: {npc}')

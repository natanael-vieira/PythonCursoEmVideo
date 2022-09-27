import random

alu1 = str(input('Digite o primeiro nome: '))
alu2 = str(input('Digite o segundo nome: '))
alu3 = str(input('Digite o terceiro nome: '))
alu4 = str(input('Digite o quarto nome: '))

lista = [alu1, alu2, alu3, alu4]

sorteado = random.choice(lista)

print(f'O Aluno que vai apagar o quadro vai ser {sorteado}.')

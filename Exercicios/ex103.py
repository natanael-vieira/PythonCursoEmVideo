print('===== FICHA JOGADOR =====\n')


def ficha(jog = '<desconhecido>', gol = 0):
    print(f'\nO jogador {jog} fez {gol} gol(s) no campeonato.')



# Programa Principal
nome = str(input('Digite o nome do jogador: ')).title()
gols = str(input('Quantos gols marcados? '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols == 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

print('===== APROVEITAMENTO JOGADOR =====')

time = []
jogador = {}
partidas = []
while True:
    print()
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: ')).title()
    tot = int(input(f'\nQuantas partidads {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [N/S]')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO! Digite N ou S.')
    if resp == 'N':
        break
print()
print('=' * 40)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('=' * 40)

while True:
    busca = int(input('Mostrar detalhes de qual jogador? [999 - FECHAR]'))
    if busca == 999:
        print('Programa encerrado!')
        break
    if busca >= len(time):
        print('ERRO! Código jogador inválido!')
    else:
        print(f' == Detalhes do jogaro {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('=' * 40)
    
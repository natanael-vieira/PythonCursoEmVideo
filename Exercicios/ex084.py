print('===== NOME E PESO =====')

pessoas = []
dado = []
mai = men = 0

while True:
    dado.append(str(input('\nDigite um nome: ')))
    dado.append(float(input('Digite um peso: ')))
    if len(pessoas) == 0:
        mai = men = 0
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    resp = str(input('\nQuer continuar? [S/N] '))
    pessoas.append(dado[:])
    dado.clear()

    if resp in 'Nn':
        break

print(pessoas)
print(f'\nForam cadastradas {len(pessoas)} pessoas')
print(f'O MAIOR peso foi de {mai}Kg. E foi de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O MENOR peso foi de {men}Kg. E foi de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')

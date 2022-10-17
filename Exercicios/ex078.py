print('===== VALORES MAIORES E MENORES EM POSIÇÃO =====\n')

val = []

for v in range(0, 5):
    val.append(int(input('Digite um número: ')))
    if v == 0:
        mai = men = val[v]
    else:
        if val[v] > mai:
            mai = val[v]
        if val[v] < men:
            men = val[v]


print('\n================================================\n')
print(f'Você digitou os valores {val}')
print(f'O MAIOR valor digitado foi {mai} e está na(s) posição(ões) ', end='')
for m, v in enumerate(val):
    if v == mai:
        print(f'{m} ', end='')
print()
print(f'O MENOR valor digitado foi {men} e está na(s) posição(ões) ', end='')
for m, v in enumerate(val):
    if v == men:
        print(f'{m} ', end='')
print('===== VÁRIOS NÚMEROS E ORGANIZAR =====')

list = []

while True:
    list.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'Nn':
        break

print(f'Foram digitados {len(list)} números')
list.sort()
list.reverse()
print(f'Os números digitados em ordem decrescente foi: {list}')

if 5 in list:
    print('Nesta lista contém o número 5!')
else:
    print('Não foi digitado nenhuma vez o número 5!')

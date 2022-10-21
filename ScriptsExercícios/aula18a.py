# teste = []
# teste.append('Natanael')
# teste.append(35)
# print(teste)
# galera = []
# galera.append(teste[:])
# print(galera)
# teste[0] = 'Abigail'
# teste[1] = 4
# galera.append(teste[:])
# print(galera)


# galera = [['Natanael', 35], ['Thais', 35], ['Abigail', 4], ['Rute', 0.3]]
# print(galera)
# print(galera[0])
# print(galera[0][0])
# print(galera[2][1])

# for p in galera:
#     print(p)
# for p in galera:
#     print(p[0])
# for p in galera:
#     print(p[1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')


galera = []
dado = []

for g in range(0, 4):
    dado.append(str(input('\nDigite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()

print()
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

mai = men = 0
print()
for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é MAIOR de idade.')
        mai +=1
    else:
        print(f'{i[0]} é MENOR de idade.')
        men += 1
print(f'\nTemos {mai} MAIORES e {men} MENORES de idade.\n')

print('===== MÉDIA DOS ALUNOS =====')

cadastro = list()

while True:
    nome = str(input('\nDigite o nome do aluno: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    cadastro.append([nome, [n1, n2], media])

    resp = str(input('\nQuer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=' * 26)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')



while True:
    print('=' * 26)
    notaInd = int(input('Mostrar notas de qual aluno? [999 PARA] '))
    if notaInd == 999:
        print('\nOperação finalizada!')
        break
    if notaInd <= len(cadastro) - 1:
        print(f'\nNotas de {cadastro[notaInd][0]} são: {cadastro[notaInd][1]}')
print('Até breve!')
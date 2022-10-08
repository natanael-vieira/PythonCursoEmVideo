n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = 0
while op != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR E MENOR
    [4] ESCOLHER OUTROS NÚMEROS
    [5] SAIR
    ''')
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print(f'\nA SOMA dos números {n1} e {n2} é: {(n1+n2)}\n')
    if op == 2:
        print(f'\nA MULTIPLICAÇÃO dos números {n1} e {n2} é: {(n1*n2)}\n')
    if op == 3:
        if n1 > n2:
            print(f'\nEntre os números {n1} e {n2}: {n1} é MAIOR\n')
        else:
            print(f'\nEntre os números {n1} e {n2}: {n2} é MAIOR\n')
    if op == 4:
        n1 = int(input('\nDigite outro número: '))
        n2 = int(input('Digite outro número: '))

print('\nPrograma ENCERRADO!\n')

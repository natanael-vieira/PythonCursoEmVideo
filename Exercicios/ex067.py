print('===== TABUADA =====')

n = 0

while True:
    n = int(input('\nDigite um número para calcular a tabuada dele: '))
    if n < 0:
        print('\nPrograma ENCERRADO')
        break
    for c in range(0, 11):
        print(f'{n} X {c} = {(n * c)}')

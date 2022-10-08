import random

cont = 0

while True:
    n = int(input('Digite um número: '))
    pc = random.randint(0, 10)
    s = n + pc
    t = ' '
    while t not in 'PI':
        t = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    
    print(f'VOCÊ escolheu {n} e o COMPUTADOR {pc}. Total {s}')

    if t == 'P':
        if s % 2 == 0:
            print('Deu PAR, VOCÊ GANHOU!')
            cont += 1
        else:
            print('Deu ÍMPAR. VOCÊ PERDEU!')
            break
    elif t == 'I':
        if s % 2 == 1:
            print('Deu ÍMPAR, VOCÊ GANHOU!')
            cont += 1
        else:
            print('Deu PAR. VOCÊ PERDEU!')
            break
    print('\nVamos jovar novamente!\n')

print(f'VOCÊ GANHOU {cont} vezes!')
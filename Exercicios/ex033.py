n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = int(input('Digite o terceiro número inteiro: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o MAIOR!')
elif n2 > n1 and n2 > n3:
    print(f'O número {n2} é o MAIOR!')
elif n3 > n1 and n3 > n2:
    print(f'O número {n3} é o MAIOR!')

if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o MENOR!')
elif n2 < n1 and n2 < n3:
    print(f'O número {n3} é o MENOR!')
elif n3 < n1 and n3 < n2:
    print(f'O número {n3} é o MENOR!')

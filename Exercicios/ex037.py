print('===== TRANSFORMAR NÚMEROS =====\n')

num = int(input('Digite um número qualquer: '))
esc = int(input('Escolha um número entre: \n1 - BINÁRIO \n2 - OCTAL \n3 - HEXADECIMAL: '))

if esc == 1:
    bi = bin(num)
    print(f'O número {num} em BINÁRIO é {bi[2:]}')
elif esc == 2:
    oc = oct(num)
    print(f'O número {num} em OCTAL é {oc[2:]}')
elif esc == 3:
    he = hex(num)
    print(f'O número {num} em HEXADECIMAL é {he[2:]}')
else:
    print('Digite uma opção válida!')

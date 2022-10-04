print('===== TRANSFORMAR NÚMEROS =====\n')

num = int(input('Digite um número qualquer: '))
esc = int(input('Escolha um número entre 1, 2 ou 3: '))

if esc == 1:
    bi = bin(num)
    print(bi)
elif esc == 2:
    oc = oct(num)
    print(oc)
elif esc == 3:
    he = hex(num)
    print(he)
else:
    print('Digite uma opção válida!')

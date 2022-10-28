# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}\n')


# #Programa Principal
# soma(5, 0)
# soma(3, 9)
# soma(1, 2)
# soma(b=1, a=2)


# def contador(* num):
#     print(num)
#     tam = len(num)
#     print(f'Recebi os valores {num} e ao todo são {tam} números.')
#     for valor in num:
#         print(f'{valor} ', end='')
#     print('FIM\n')


# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2, 3)


# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos +=1


# valores = [6, 3, 9, 1, 0, 2]
# print(valores)
# dobra(valores)
# print(valores)


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos como resultado da soma: {s}')


soma(5, 2)
soma(9, 6, 5)

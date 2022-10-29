print('===== VALIDAÇÃO DE NÚMEROS =====\n')


def leiaInt(n):
    while True:
        print(n, end='')
        num = str(input())
        
        if num.isnumeric():
            n = num
            return n
        else:
            print('ERRO! Digite um número válido.\n')



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou e digitar o número {n}')
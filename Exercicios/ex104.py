print('===== VALIDAÇÃO DE NÚMEROS =====\n')


def leiaInt(n):
    while True:
        print(n, end='')
        num = str(input())
        
        if num.isnumeric():
            n = num
            return n
        else:
            print('\033[0;35mERRO! Digite um número VÁLIDO.\033[m\n')



# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou e digitar o número {n}')
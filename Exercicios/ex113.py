print('===== VALIDAÇÃO DE NÚMEROS =====\n')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\nERRO! Digite um número INTEIRO VÁLIDO!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados INTERROMPIDA!')
            return 0
        else:
            return n

    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\nERRO! Digite um número DECIMAL VÁLIDO!')
            continue
        except (KeyboardInterrupt):
            print('\nEntrada de dados INTERROMPIDA!')
            return 0
        else:
            return n


# Programa Principal
n1 = leiaInt('Digite um número INTEIRO: ')
n2 = leiaFloat('Digite um número DECIMAL: ')

print(f'\nVocê digitou o número INTEIRO {n1} e o DECIMAL {n2}')

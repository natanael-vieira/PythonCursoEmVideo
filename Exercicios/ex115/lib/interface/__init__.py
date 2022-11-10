def linha(tam = 42):
    return '=' * tam


def cab(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


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


def menu(lista):
    cab('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

# ===== TRATAMENTO DE EXCEÇÃO =====

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))

    r = a / b


except (ValueError, TypeError):
    print('Problema com o tipo de entrada de dados')


except ZeroDivisionError:
    print('Impossível divisão por ZERO')


except KeyboardInterrupt:
    print('Usuário não informou dados')


except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')


else:
    print(f'O resultado é {r:.2f}')


finally:
    print('Volte SEMPRE!')

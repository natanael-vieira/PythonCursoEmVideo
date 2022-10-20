print('===== VALIDAR EXPRESSÃO =====\n')

exp = str(input('Digite uma expressão: '))
pilha = []

for p in exp:
    if p == '(':
        pilha.append('(')
    elif p == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é VÁLIDA!')
else:
    print('Sua expressão é ÍNVÁLIDA!')

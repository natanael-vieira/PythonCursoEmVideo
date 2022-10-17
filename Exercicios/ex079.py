print('===== LISTA DE VALORES =====')

val = []

while True:
    n = int(input('Digite um valor: '))
    
    if n not in val:
        val.append(n)
    else:
        print('Valor duplicado! Não vou adicionar!')
    
    pare = str(input('Quer continuar [S/N]? '))
    if pare in 'nN':
        break
val.sort()
print(f'Os valores digitados foram: {val}')

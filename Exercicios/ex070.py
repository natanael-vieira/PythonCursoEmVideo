print('===== COMPRAS =====')

total = 0
contMil = 0
menor = 0
cont = 0
menorPre = ' '

while True:
    prod = str(input('\nDigite o PRODUTO: ')).upper().strip()
    preco = float(input('Digite o VALOR do PRODUTO: R$ '))
    cont += 1
    total += preco

    if preco > 1000.00:
        contMil += 1
    
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            menorPre = prod
    
    con = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    
    if con == 'N':
        break

print(f'O TOTAL gasto na COMPRA foi de R$ {total:.2f}')
print(f'A quantidade de produtos com valor MAIOR que R$ 1000.00 foi de {contMil}')
print(f'O produto com MENOR valor foi {menorPre}.')

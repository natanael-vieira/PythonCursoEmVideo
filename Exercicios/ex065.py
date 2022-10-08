resp = 'S'
soma = qtd = med = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]

med = soma / qtd
print(f'\nVocê digitou {qtd} números e a MÉDIA entre eles foi {med:.2f}')
print(f'\nO MAIOR número foi {maior} e o MENOR número foi {menor}')
print('\nENCERRADO!')
print('===== VERIFICAR JURO/DESCONTO =====\n')

p = float(input('Digite o valor da compra: R$ '))
pag = int(input('\nEscolha a forma de pagamento: \n1 - À vista no dinheiro/cheque \n2 - À vista no cartão \n3 - Parcelar em 2X s/ juros \n4 - Parcelar acima de 2X c/ juros\nEscolha: '))

avi = 1
aviC = 2
duasC = 3
tresC = 4

av = p - (p * 10 / 100)
avC = p - (p * 5 / 100)
pC = p + (p * 20 / 100)

if pag == avi:
    print(f'\nO valor total à vista no dinheiro/cheque com desconto é: R$ {av}')
elif pag == aviC:
    print(f'\nO valor total à vista no cartão com desconto é: R$ {avC}')
elif pag == 3:
    print(f'\nO valor total é: R$ {p} em 2X no cartão')
elif pag == 4:
    print(f'\nO valor total com jutos é: R$ {pC} acima de 3X no cartão')
else:
    print('\nForma de pagamento INVÁLIDA.')

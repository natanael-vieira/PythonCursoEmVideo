import mailbox


print('===== MAIOR E MENOR PESO =====')

mai = 0
men = 0
for i in range(1, 6):
    p = float(input(f'Digite o peso da {i}ª pessoa: '))
    if i == 1:
        mai = p
        men = p
    else:
        if p > mai:
            mai = p
        if p < men:
            men = p
print(f'O maior peso lido foi: {mai:.3f}Kg!')
print(f'O menor peso lido foi: {men:.3f}Kg!')

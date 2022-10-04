print('========== SIMULAÇÃO DE EMPRÉSTIMO ==========\n')

price = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual sua renda? R$ '))
parc = (int(input('Qual o prazo para pagamento, em anos? '))) * 12

rend = sal * 30/100
mensal = price / parc

if mensal > rend:
    print(f'\nNegado! O valor da parcela de R$ {mensal:.2f} excede os 30% da sua renda de R$ {rend:.2f} do salário de R$ {sal:.2f}')
else:
    print(f'\nAprovado! O valor da parcela será de {mensal:.2f}')

print('Obrigado pela preferência!')
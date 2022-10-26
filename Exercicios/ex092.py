from datetime import datetime

print('===== CADASTRO DE TRABALHADORES E APOSENTADORIA =====\n')

prev = {}

prev['nome'] = str(input('Digite o nome do trabalhador: ')).capitalize()
ano = int(input('Digite o ano de nascimento: '))

idade = datetime.now().year - ano
prev['idade'] = idade

prev['ctps'] = int(input('Digite o nº da CTPS: [0 - NÃO POSSUI] '))
if prev['ctps'] == 0:
    print(prev)
    print()
    for k, v in prev.items():
        print(f'{k} tem o valor {v}')
else:
    contr = int(input('Digite o ano de contratação: '))
    anosTrab = datetime.now().year - contr
    apos = 35 - anosTrab
    prev['contratação'] = contr
    prev['salario'] = float(input('Digite o salário: '))
    prev['aposentadoria'] = apos + idade

    print(prev)
    print()

    for k, v in prev.items():
        print(f'{k} tem o valor {v}')



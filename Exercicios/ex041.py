import datetime

print('===== CONFEDERAÇÃO DE NATAÇÃO =====\n')

ano = int(input('Digite o ano do seu nascimento: '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
idade = int(year) - ano

if idade <= 9:
    print(f'Você tem {idade} anos, portanto sua categoria é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos, portanto sua categoria é INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos, portanto sua categoria é JÚNIOR.')
elif idade <= 20:
    print(f'Você tem {idade} anos, portanto sua categoria é SÊNIOR.')
else:
    print(f'Você tem {idade} anos, portanto sua categoria é MASTER.')

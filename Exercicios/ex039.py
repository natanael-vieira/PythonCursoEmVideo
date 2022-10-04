import datetime

print('===== SERVIÇO MILITAR =====\n')

ano = int(input('Digite o ano do seu nascimento: '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
idade = int(year) - ano

if idade == 18:
    print(f'\nEsse é seu ano de se alistar, pois possui ou vai completar {idade} anos.')
elif idade > 18:
    print('\nVocê está em débito com o serviço militar, já passou da idade de se alistar. Compareça a uma unidade militar para se regularizar.')
else:
    print('\nVocê ainda não está na idade de se alistar!')

import datetime
from tkinter.filedialog import SaveFileDialog

print('===== SERVIÇO MILITAR =====\n')

ano = int(input('Digite o ano do seu nascimento: '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
idade = int(year) - ano

prazo = idade - 18

if idade == 18:
    print(f'\nEsse é seu ano de se alistar, pois possui ou vai completar {idade} anos este ano.')
elif idade > 18:
    print(f'\nVocê está em débito com o serviço militar, já se passou {prazo} anos do alistamento. Compareça a uma unidade militar para se regularizar.')
else:
    saldo = 18 - idade
    print(f'\nVocê ainda não está na idade de se alistar, falta(m) {saldo} ano(s) para o alistamento!')

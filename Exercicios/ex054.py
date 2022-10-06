import datetime

print('===== MAIORIDADE =====\n')

date = datetime.date.today()
year = date.strftime("%Y")
ano = int(year)

idade = 0
mai = 0
men = 0
for a in range(1, 8):
    a = int(input('Digite o ano de nascimento: '))
    idade = ano - a
    if idade >= 21:
        mai += 1
    elif idade < 21:
        men +=1

print(f'Existem {mai} pessoas maiores de idade!')
print(f'E temos também {men} pessoas menores de idade!')

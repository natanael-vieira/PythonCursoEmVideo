print('===== NOMES, IDADES E GÊNEROS =====')

s = 0
m = 0
mIdH = 0
noHoV = ''
qtdM = 0

for i in range(1, 5):
    nome = str(input(f'\nDigite o nome da {i}ª pessoa: ')).upper()
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    gen = str(input(f'Digite o gênero da {i}ª pessoa: ')).upper()
    s += idade
    qtdM = len(gen)

    if i == 1 and gen == 'M':
        mIdH = idade
        noHoV = nome
    if gen == 'M' and idade > mIdH:
        mIdH = idade
        noHoV = nome
    if gen == 'F' and idade < 20:
        qtdM += 1

        
m = s / 4
print(f'A MÉDIA de idade do grupo é de {m:.0f} anos!')
print(f'O nome do HOMEM mais velho é {noHoV} e ele tem {mIdH} anos!')
print(f'A quantidade de MULHERES com menos de 20 anos é {qtdM}!')
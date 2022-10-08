print('===== CADASTRO =====\n')

contIdade = 0
contHom = 0
contMul = 0

while True:
    idade = int(input('Digite a idade da pessoa: '))
    gen = str(input('Digite o gênero da pessoa [M/F]: ')).upper().strip()[0]
    
    if idade > 18:
        contIdade += 1
    if gen == 'M':
        contHom +=1
    if gen == 'F' and idade < 20:
        contMul += 1
    con = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    
    if con == 'N':
        break

print(f'Foram cadastradas {contIdade} MAIORES de 18 anos.')
print(f'Foram cadastrados {contHom} HOMENS.')
print(f'Foram cadastradas {contMul} MULHERES com MENOS de 20 anos.')

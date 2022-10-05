import random

print('===== PEDRA-PAPEL-TESOURA =====\n')

print('Já fiz a minha escolha, agora é sua vez. VAMOS JOGAR!!!\n')
esc = str(input('Pedra, Papel ou Tesoura? ')).upper()

pc = random.randint(1,3)

if pc == 1:
    pc = 'PEDRA'
    if pc == 'PEDRA' and esc == 'PEDRA':
        print(f'EMPATAMOS! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'PEDRA' and esc == "PAPEL":
        print(f'VOCÊ GANHOU! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'PEDRA' and esc == 'TESOURA':
        print(f'EU GANHEI! Eu escolhi {pc} e você {esc}\n')
elif pc == 2:
    pc = 'PAPEL'
    if pc == 'PAPEL' and esc == 'PAPEL':
        print(f'EMPATAMOS! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'PAPEL' and esc == "TESOURA":
        print(f'VOCÊ GANHOU! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'PAPEL' and esc == 'PEDRA':
        print(f'EU GANHEI! Eu escolhi {pc} e você {esc}\n')
elif pc == 3:
    pc = 'TESOURA'
    if pc == 'TESOURA' and esc == 'TESOURA':
        print(f'EMPATAMOS! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'TESOURA' and esc == "PEDRA":
        print(f'VOCÊ GANHOU! Eu escolhi {pc} e você {esc}\n')
    elif pc == 'TESOURA' and esc == 'PAPEL':
        print(f'EU GANHEI! Eu escolhi {pc} e você {esc}\n')

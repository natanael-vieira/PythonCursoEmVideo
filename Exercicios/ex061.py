print('===== PROGRESSÃO ARITMÉTICA =====\n')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('\nDigite a razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print(termo)
    termo += razao
    cont += 1
    
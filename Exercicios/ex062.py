print('===== PROGRESSÃO ARITMÉTICA =====\n')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo)
        termo += razao
        cont += 1
    mais = int(input('Quantos termos você quer mostrar a mais? '))

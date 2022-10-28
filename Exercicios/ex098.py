from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    
    if passo == 0:
        passo = 1

    print('=' * 40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('=' * 40)
print('\nAgora é sua vez, escolha os valores a seguir: \n')
i = int(input('Digite o INÍCIO: '))
f = int(input('Digite o FIM: '))
p = int(input('Digite o PASSO: '))

contador(i, f, p)

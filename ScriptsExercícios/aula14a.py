n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n!=0:
        if n %2 == 0:
            par +=1
        else:
            impar += 1
print(f'\nVocê digitou {par} números pares e {impar} números ímpares!')
print('\nChegou ao final!\n')

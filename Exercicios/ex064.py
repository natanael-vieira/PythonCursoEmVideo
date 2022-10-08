num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 PARA]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 PARA]: '))
print(f'\nVocê digitou {(cont)} números e a SOMA entre eles foi {soma}.')
print('ENCERROU')
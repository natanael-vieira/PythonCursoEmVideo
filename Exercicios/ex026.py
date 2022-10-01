frase = input('Digite uma frase: ').upper().strip()
vezes = frase.count('A')
find = frase.find('A')+1
rfind = frase.rfind('A')+1
print(f'A quantidade de vezes que a letra A aparece é: {vezes}.')
print(f'A primeira vez que a letra A aparece é na posição: {find}.')
print(f'A última letra A apareceu na posição: {rfind}.')
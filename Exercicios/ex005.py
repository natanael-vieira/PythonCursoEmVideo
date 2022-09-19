n1 = int(input('Digite um valor:\n'))
n2 = int(input('Digite outro valor:\n'))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
rd = n1 // n2
e = n1 ** n2
mod = s%2

print(f'A soma dos dois números é {s}. A subtração é {sub}. A multiplicação é {m}!')
print(f'A divisão dos dois números é {d}. Já divisão inteira é {rd}. A exponenciação é {e}.')
print(f'O módulo da soma por 2 é {mod}')

print('='*100)

num1 = int((input('Digite um número qualquer: ')))
ant = num1 - 1
suc = num1 + 1

print(f'O antecessor de {num1} é {ant} e seu sucessor é {suc}')

n = s = c = 0

while True:
    n = int(input('Digite um número [999 PARAR]: '))
    if n == 999:
        break
    s += n
    c += 1

print(f'\nA quantidade de números digitados foi {c} e a SOMA deles foi {s}.\n')
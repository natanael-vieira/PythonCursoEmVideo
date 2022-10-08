print('===== FIBONACCI =====')
n = int(input('Digite quantos termos você quer mostrar: '))
t1 = 0
t2 = 1

print(t1)
print(t2)

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(t3) 
    t1 = t2
    t2 = t3
    cont +=1
print('FIM')
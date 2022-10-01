nome = str(input('Digite seu nome completo: ')).strip().title()
n = nome.split()
fname = n[0]
lname = n[len(n)-1]

print('Muito prazer em conhecer você!')
print(f'Seu primeiro nome é: {fname}')
print(f'Seu último nome é: {lname}')

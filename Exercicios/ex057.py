gen = ''
while gen != 'F' and gen != 'M':
    gen = str(input('Digite seu gênero [M/F]: ')).upper()
    if gen != 'M' and gen != 'F':
        print('Gênero inválido! Tente novamente!')
print(f'O gênero selecionado foi {gen}!')
print('='*40)
print(f'{"FATIANDO TUPLAS":^40}')
print('='*40)

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for w in words:
    print(f'\nNa palavra {w} temos as vogais: ', end='')
    for l in w:
        if l.lower() in 'aeiou':
            print(l.lower(), end=' ')

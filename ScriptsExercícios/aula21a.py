# help() - Aula sobre ajuda interativa, colocar para que ser a função que foi criada, 
# ou outro motivo qualquer que queira colocar na função help().

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :parâmetro i: início da contagem
    :parâmetro f: fim da contagem
    :parâmetro p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


# Programa Principal
help(contador)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Parâmetro Opcional
# Para usar os parâmetros opcionais, basta atribuir ao parâmetro o valor 'zero' 0
def somar(a=0, b=0, c=0):  
    """
    => Faz a soma de três valores e mostra o resultado na tela.
    :parâmetro a: o primeiro valor
    :parâmetro b: o segundo valor
    :parâmetro c: o terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')


# Programa Principal
somar(3, 2, 5)
somar(8, 4)
somar(c=2, a=15)
somar(b=100, a=-99)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Escopo da Função (Global e Local)
# Função def é escopo Local
# Função Principal é escopo Global
def teste(b): 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


# Programa Principal
a = 5
teste(a)
print(f'A fora vale {a}')



def teste(e):
    global d
    d = 8
    e += 4
    f = 2
    print(f'D dentro vale {d}')
    print(f'E dentro vale {e}')
    print(f'F dentro vale {f}')


# Programa Principal
d = 5
teste(d)
print(f'D fora vale {d}')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Função com retorno, sempre usa return para usar o resultado da função
def somar(l = 0, m = 0, n = 0):
    s = l + m + n
    return s


# Programa Principal
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(37)

print(f'Meus cálculos resultaram em {r1}, {r2} e {r3}.')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# Programa Principal
n = int(input('Digite um número para saber seu fatorial: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2} e {f3}.')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def parOuImpar(n=0):
    if n %2 == 0:
        return True
    else: 
        return False 


# Programa Principal
num = int(input('Digite um número: '))

if parOuImpar(num):
    print('É PAR!')
else:
    print('É ÍMPAR!')

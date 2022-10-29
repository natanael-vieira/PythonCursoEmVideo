print('===== PRECISO VOTAR? =====\n')

def votar(ano):
    from datetime import date
    idade = date.today().year - ano
 
    if idade < 16:
        return f'Com {idade} anos de idade NÃO VOTA!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos de idade o VOTO É FACULTATIVO!'
    elif idade >= 18 and idade < 65:
        return f'Com {idade} anos de idade o VOTO É OBRIGATÓRIO!'
    elif idade >= 65:
        return f'Com {idade} anos de idade o VOTO É FACULTATIVO!'


#Programa Principal

ano = int(input('Digite seu ano de nascimento: '))
votar(ano)
print(votar(ano))

print('===== CADASTRO DE PESSOAS =====')


cadastro = []
pessoa = {}
soma = media = 0
while True:
    print()
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    
    while True:
        pessoa['genero'] = str(input('Gênero: [F/M] ')).upper()
        if pessoa['genero'] in 'MF':
            break
        print('ERRO! Digite F ou M.')
    
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    cadastro.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [N/S] ')).upper()
        if resp in 'NS':
            break
        print('ERRO! Digite N ou S.')
    if resp == 'N':
        break
print('=' * 30)
print(cadastro)
print('=' * 30)
print(f'Ao todo temos {len(cadastro)} pessoas cadastradas.')
print('=' * 30)
media = soma / len(cadastro)
print(f'A média das idades das pessoas cadastrasdas é de: {media:.2f}')
print('=' * 30)
print('As mulheres cadastradas foram: ', end='')
for p in cadastro:
    if p['genero'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('=' * 30)
print('A lista das pessoas que tem idade acima da média: ', end='')
for i in cadastro:
    if i['idade'] >= media:
        print(f'{i["nome"]} ', end='')
print()
print('=' * 30)

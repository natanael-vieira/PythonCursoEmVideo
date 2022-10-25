pessoas = {'nome': 'Natanael', 'sexo': 'M', 'idade': 35}
print(pessoas)
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for v in pessoas.values():
    print(v)

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} : {v}')

pessoas['nome'] = 'Thais'

for k, v in pessoas.items():
    print(f'{k} : {v}')

pessoas['sexo'] = 'F'
pessoas['peso'] = 74.6

for k, v in pessoas.items():
    print(f'{k} : {v}')

print()

brasil = []
estado1 = {'uf': "Santa Catarina", 'sigla': 'SC'}
estado2 = {'uf': "Goias", 'sigla': 'GO'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
print(brasil[1]['sigla'])
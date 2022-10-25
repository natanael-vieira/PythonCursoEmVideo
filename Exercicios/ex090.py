print('===== VERIFICAR SITUAÇÃO DO ALUNO =====\n')

dados = {}
aluno = []

dados['nome'] = str(input('Nome do aluno: ')).capitalize()
dados['media'] = float(input('Média final: '))
aluno.append(dados.copy())

print()

print(f'Nome é igual {aluno[0]["nome"]}')
print(f'Média é igual {aluno[0]["media"]}')

if dados['media'] >= 7.0:
    print('Aluno APROVADO!')
else:
    print('Aluno REPROVADO!')
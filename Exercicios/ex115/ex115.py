from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'teste.txt'


if arquivoExiste(arq):
    print('Arquivo EXISTENTE!')
else:
    print('Arquivo INEXISTENTE!')
    criarArquivo(arq)


while True:
    resp = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'SAIR do Sistema'])

    if resp == 1: # Lista o conteúdo do arquivo
        lerArquivo(arq)
    elif resp == 2: # Cadastra uma nova pessoa
        cab('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3: # Sai do sistema
        sleep(1)
        cab('Saindo do Sistema. Até logo!')
        sleep(1)
        break
    else: # Digitou errado
        cab('ERRO! Digite uma opção válida!')
    sleep(1)

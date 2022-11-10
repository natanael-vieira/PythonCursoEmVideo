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

    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cab('CADASTRAR NOVA PESSOA')
    elif resp == 3:
        sleep(1)
        cab('Saindo do Sistema. Até logo!')
        sleep(1)
        break
    else:
        cab('ERRO! Digite uma opção válida!')
    sleep(1)

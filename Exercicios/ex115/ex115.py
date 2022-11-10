from lib import interface
from time import sleep


while True:
    resp = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'SAIR do Sistema'])

    if resp == 1:
        interface.cab('PESSOAS CADASTRADAS')
    elif resp == 2:
        interface.cab('CADASTRAR NOVA PESSOA')
    elif resp == 3:
        sleep(1)
        interface.cab('Saindo do Sistema. Até logo!')
        sleep(1)
        break
    else:
        interface.cab('ERRO! Digite uma opção válida!')
    sleep(1)

print('===== ANALISANDO DICIONÁRIOS =====\n')


def notas(*n, sit=False):
    """
    => Função para analisar notas e situação dos alunos de uma turma.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional que indica se deve ou não incluir a situação no dicionário.
    :return: dicionário com informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


# Programa Principal
resp = notas(5.5, 4.1, 6.1, 3.5, sit=True)

print(resp)
help(notas)

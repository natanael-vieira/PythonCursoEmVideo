print('===== BRASILEIRÃO 2022 =====\n')

bra = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense', 'Atético-PR', 'Atlético-MG', 'América-MG', 'Botafogo', 'Fortaleza', 'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print(f'Os cinco primeiros colocados do Brasileirão 2022 são: {bra[:5]}\n')
print(f'Os quatro últimos colocados são: {bra[16:]}\n')
print(sorted(bra))
print(f'\nO Avaí está na {bra.index("Avaí")+1}ª posição.')
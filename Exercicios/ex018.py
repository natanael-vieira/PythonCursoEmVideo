import math

ang = int(input('Digite o valor do ângulo (entre 0º e 360º): '))

sen = math.sin(ang)
cos = math.cos(ang)
tg = math.tan(ang)

print(f'O ângulo de {ang}º tem o seno {sen:.2f}, o cosseno {cos:.2f} e a tangente {tg:.2f}.')

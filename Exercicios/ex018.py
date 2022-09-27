import math

ang = int(input('Digite o valor do ângulo (entre 0º e 360º): '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print(f'O ângulo de {ang}º tem o seno {sen:.2f}, o cosseno {cos:.2f} e a tangente {tg:.2f}.')

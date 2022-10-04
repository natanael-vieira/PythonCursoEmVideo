print('=== Analisando triângulos ===\n')

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'\nOs segmentos {s1}, {s2} e {s3} PODEM FORMAR um TRIÂNGULO!')
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('Este é um triângulo EQUILÁTERO.\n')
    elif s1 == s2 and s1 != s3 or s1 == s3 and s1 != s2 or s2 == s3 and s2 != s1:
        print('Este é um triângulo ISÓSCELES.\n')
    elif s1 != s2 and s1 != s3 and s2 != s3:
        print('Este é um triângulo ESCALENO.\n')
else:
    print(f'\nOs segmentos {s1}, {s2} e {s3} NÃO PODEM FORMAR um TRIÂNGULO!')
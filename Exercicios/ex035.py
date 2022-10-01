print('=== Analisando triângulos ===')

s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'Os segmentos {s1}, {s2} e {s3} PODEM FORMAR um TRIÂNGULO!')
else:
    print(f'Os segmentos {s1}, {s2} e {s3} NÃO PODEM FORMAR um TRIÂNGULO!')

metro = float(input('Digite a metragem: '))
cm = metro * 100
mm = metro * 1000
km = metro / 1000
dam = metro / 100
dm = metro * 10 

print(f'A medida {metro}m tem: \n{km}km \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm.')

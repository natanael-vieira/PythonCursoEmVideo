dias = int(input('Porquantos dias o carro foi alugado? '))
km = float(input('Quantos quilômentros (km) o carro rodou? '))
pagar = (dias * 60) + (km *0.15)

print(f'O carro foi alugado por {dias} dias e rodou {km:.2f}km. Portanto o valor final do aluguel é de R${pagar:.2f}')
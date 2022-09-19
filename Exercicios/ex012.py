preco = float(input('Digite o preço do produto: '))
desc = preco - (preco * (5/100))

print(f'O preço do produto é de R${preco:.2f}, mas com o desco de 5% fica R${desc:.2f}')
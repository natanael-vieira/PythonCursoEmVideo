preco = float(input('Digite o preço do produto: R$ '))
desc = preco - (preco * (5/100))

print(f'O preço do produto é de R${preco:.2f}, mas com o desconto de 5% fica R${desc:.2f}')
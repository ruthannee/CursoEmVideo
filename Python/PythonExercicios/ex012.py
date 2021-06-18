#ler preco de um produto e imprimir com 5% de desconto
preco = float(input("Digite o preco do produto: R$"))
desconto = preco - (preco * 0.05)
print("Seu produto recebeu 5% de desconto, totalizando R${:.2f}.".format(desconto))
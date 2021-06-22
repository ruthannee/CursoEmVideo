carteira = float(input("Digite o valor que tem na carteira: R$"))
dolar = carteira / 5.12
print("Com R${:.2f}, você pode comprar US${:.2f}.".format(carteira, dolar))
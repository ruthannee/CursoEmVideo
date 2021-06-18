km = float(input("Quantos KM foram rodados? "))
dias = int(input("Por quantos dias? "))
pago = (km * 0.15) + (dias * 60)
print("Total a pagar é: R${:.2f}.".format(pago))
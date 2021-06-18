#ler largura e altura de uma parede, em metros, calcular a área e a qtd de tinta para pintá-la
#(cada litro de tinta pinta uma área de 2m²)
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
print("Sua parede tem a dimensão de {}x{} e sua área tem {:.3f}m².".format(largura, altura, area))
print(f"Para pintar a parede, será preciso {area/2}L de tinta.")
#ler valor em metros e exibir em centímetros e milímetros
medida = float(input("Distância em metro(s): "))
cm = medida * 100
mm = medida * 1000
print(f"A medida {medida} corresponde a {cm:.0f}cm e {mm:.0f}mm.")
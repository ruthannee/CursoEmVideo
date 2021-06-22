frase = str(input("Digite uma frase: ")).lower().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
print("Primeira posição: {}".format(frase.find("a")+1))
print("Última posição: {}".format(frase.rfind("a")+1))

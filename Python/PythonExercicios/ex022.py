nome = str(input("Digite um nome completo: ")).strip()
#MAIÚSCULA
print(nome.upper())

#MINÚSCULA
print(nome.lower())

#QUANTAS LETRAS, SEM CONSIDERAR OS ESPAÇOS
print(len(nome)-nome.count(' '))

#QUANTAS LETRAS NO PRIMEIRO NOME
print(nome.find(' '))
#OU
separado = nome.split()
print(len(separado[0]))
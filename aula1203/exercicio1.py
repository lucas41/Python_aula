nome = input("qual o seu nome ?")

print("vamos imprimir seu nome")

quant = len(nome)

cont = 0

while (cont <= quant):
    print(nome[0: cont])
    cont += 1
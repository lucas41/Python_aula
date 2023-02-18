livro =  int(input("quantos livros você desejaria comprar?  "))

tipo1 = 0
tipo2 = 0

while ( livro > 0):

    tipo1 = tipo1 + 0.25
    tipo2 = tipo2 + 0.50
    livro = livro - 1;


tipo1final = tipo1 + 7.5
tipo2final = tipo2 + 2.5


if(tipo1final < tipo2final):
    print("o tipo de maior vantagem e o tipo 1")
else:
    print("o tipo de maior vantagem e o tipo 2")

print(f"o valor final no tipo 1 de pagamento é: {tipo1final}")
print(f"o valor final no tipo 2 de pagamento é: {tipo2final}")
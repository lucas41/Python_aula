media = 0

while (media >= 0):

    media = int(input("Insira a média que deseja calcular"))

    if(media >= 5):
        print("aluno aprovado")
    elif(media >= 3):
        print("aluno em RE")
    else:
        print("aluno reprovado")


print("programa finalizado")
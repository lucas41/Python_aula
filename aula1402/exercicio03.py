print("olá bem vindo")

lopp = "sim"

while (lopp == "sim"):

    nome = input("Insira seu nome: ")
    RG = input("Insira seu RG: ")
    CPF = input("Insira seu CPF: ")
    celular = input("Insira seu celular: ")
    Email = input("Insira seu Email: ")

    print(f"olá {nome} seu RG é {RG} e seu CPF é {CPF} seu numero de celular é {celular} e seu email é {Email}")

    lopp = input("deseja cadastrar um novo cadastro? SIM ou NÃO")
    
else:
    print("fim da aplicação")


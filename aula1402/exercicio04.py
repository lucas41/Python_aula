val1 = input("insira o valor 1: ")
val2 = input("insira o valor 2: ")

val1int = int(val1)
val2int = int(val2)

val1double = val1int * 2
multi = val1int * val2int
resto = val1int % val2int
divi = val1int / val2int
potencia = val1int ^ val2int
raiz = val2int ** (1/2)

print(f"O dobro do primeiro valor é {val1double}")
print(f"A multiplicação dos valores é {multi}")
print(f"O resto da divisão entre os numeros é {resto}")
print(f"A divisão dos valores é {divi}")
print(f"A potencia dos valores é {potencia}")
print(f"A raiz do segundo numero é {raiz}")


cidadeA = int(90000)
cidadeB = int(50000)

anos = int(input("qual a quantidade de anos que deseja calcular? "))

crescimento1 = (cidadeA * (0.009 * anos)) + cidadeA 
cresicmento2 = (cidadeB * (0.015 * anos)) + cidadeB

print(f"a população da cidade A sera de: {crescimento1} em {anos} anos")
print(f"a população da cidade B sera de: {cresicmento2} em {anos} anos")

if(crescimento1 > cresicmento2):
    print("A cidade A cresceu + no intervalo de tempo")
else:
    print("A cidade B cresceu + no intervalo de tempo")
data = input("insira sua data de nascimento no fomarto dd/mm/yyyy: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

mes = int(mes)
mesextenso = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

mes = mesextenso[mes]

print(f"você nasceu no dia {dia} do mês de {mes} no ano de {ano}")
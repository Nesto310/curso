while True:
    try:
        salariohora = float(input("Quanto você recebe por hora? (apenas numeros)"))
        horatrabalhada = float(input("Quantas horas você trabalha por mês? (apenas numeros)"))
        break
    except ValueError: print("Você deve colocar apenas numeros, tente novamente.")

salariototal = salariohora * horatrabalhada

print(f"Você vai receber R${salariototal} por mês.")
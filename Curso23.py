while True:
    try:
        Salario1 = float(input("Qual o salario da pessoa ?"))
        Aumento1 = float(input("Quanto ""%"" deseja dar de aumento ?"))
        break
    except ValueError: print("Por favor, coloque apenas numeros.")

Salario1 = Salario1 * Aumento1
Salario1 = Salario1 / 100

print("Você ira dar um aumento de ", Salario1)
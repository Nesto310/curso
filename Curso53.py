while True:
    try:
        numero1 = float(input("Quanto é o primeiro lado do triangulo? "))
        numero2 = float(input("Quanto é o segundo lado do triangulo? "))
        numero3 = float(input("Quanto é o terceiro lado do triangulo? "))
        break
    except ValueError: print("Coloque apenas numeros.")

soma = numero1 + numero2 + numero3

print(f"Com a soma dos lados, vai dar {soma}")
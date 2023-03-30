while True:
    try:
        numero1 = float(input("Qual o numero que você quer que eu some ?"))
        numero2 = float(input("Qual o outro numero que você quer que eu some?"))
        break
    except ValueError: print("Tente colocar apenas numeros.")

soma = numero1 + numero2

print(f"Opa, a soma total deu {soma}")
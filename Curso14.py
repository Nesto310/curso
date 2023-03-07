try:
    Numero1 = float(input("Qual numero que é ? "))
except ValueError: print("Você deve apenas colocar numeros!")

try:
    if Numero1 >= 0:
        print("O numero", Numero1, "é positivo")
    else:
        print("O numero", Numero1, "é negativo")
except NameError: print("Tente novamente.")
try:
    Numero1 = float(input("Diga um numero? "))
except ValueError: print("Você deve digitar apenas numeros!")

try:
    Numero2 = float(input("Diga um outro numero? "))
except ValueError: print("Você deve digitar apenas numeros!")

try:
    if Numero1 > Numero2:
        print("O numero", Numero1, "é maior que o numero", Numero2)
    else:
        print ("O numero", Numero2, "é maior que o numero", Numero1)
except NameError: print("Tente novamente, você deve apenas colocar numeros.")
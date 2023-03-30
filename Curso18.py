while True:
    try:
        Numero1 = float(input("Qual o primeiro Numero? "))
        Numero2 = float(input("Qual o segundo Numero? "))
        Numero3 = float(input("Qual o terceiro Numero? "))
        break
    except ValueError: print("Tente apenas numeros!")

if Numero1 > Numero2 and Numero1 > Numero3:
    print(Numero1, " é maior que os outros")
elif Numero2 > Numero1 and Numero2 > Numero3:
    print(Numero2, "é maior que os outros")
else:
    print(Numero3, "é maior que os outros")
if Numero1 < Numero2 and Numero1 < Numero3:
    print("e o numero ", Numero1, "é o menor de todos")
elif Numero2 < Numero1 and Numero2 < Numero3:
    print("e o numero", Numero2, "é o menor de todos")
else:
    print("e o numero", Numero3, "é o menor de todos")
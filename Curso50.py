while True:
    try:
        numero1 = float(input("Qual o primeiro numero? "))
        numero2 = float(input("Qual o segundo numero? "))
        numero3 = float(input("Qual o terceiro numero? "))
        break
    except ValueError: print("Deve responder as perguntas com apenas numeros!")

if numero1 > numero2 and numero1 > numero3:
    print(f"O numero {numero1} é maior que todos.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O numero {numero2} é maior que todos.")
else:
    print(f"O numero {numero3} é maior que todos.")

if numero1 <= numero2 and numero1 <= numero3:
    print(f"O numero {numero1} é o menor de todos.")
elif numero2 <= numero3 and numero2 <= numero1:
    print(f"O numero {numero2} é o menor de todos.")
elif numero3 <= numero2 and numero3 <= numero1:
    print(f"O numero {numero3} é o menor de todos.")
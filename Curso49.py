while True:
    try:
        numero1 = float(input("Qual o primeiro numero? "))
        numero2 = float(input("Qual o segundo numero? "))
        numero3 = float(input("Qual o terceiro numero? "))
        break
    except ValueError: print("Coloque apenas numeros.")

if numero1 > numero2 and numero1 > numero3:
    print(f"O numero {numero1} é o maior de todos.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"O numero {numero2} é o maior de todos.")
else:
    print(f"O numero {numero3} é o maior de todos.")
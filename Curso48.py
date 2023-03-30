while True:
    try:
        numero1 = float(input("Me fale um numero ? "))
        numero2 = float(input("Me fale outro numero ? "))
        break
    except ValueError: print("coloque apenas numeros.")

if numero1 > numero2:
    print(f"O numero {numero1} é maior que o {numero2}")
elif numero2 == numero1:
    print("Os numeros são iguais.")
else: print(f"O numero {numero2} é maior que o {numero1}")
while True:
    try:
        Dias = int(input("Quantos dias tem o ano ? "))
        break
    except ValueError: print("apenas numeros!")

if Dias == 365:
    print("esse ano não é bisexto")
elif Dias == 366:
    print("esse ano é bisexto")
else:
    print("Coloque apenas numeros de dias do ano corretamente.")
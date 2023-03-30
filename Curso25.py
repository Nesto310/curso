while True:
    try:
        Nota1 = float(input("Qual sua primeria nota ? "))
        Nota2 = float(input("Qual sua segunda nota? "))
        break
    except ValueError: print("Valor invalido, coloque apenas numeros.")

Media = Nota1 + Nota2
Media = Media / 2

print("Sua media é", Media)
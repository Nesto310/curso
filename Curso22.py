while True:
    try:
        Lado1 = float(input("Me diga o primeiro lado? "))
        Lado2 = float(input("Me diga o segundo lado? "))
        Lado3 = float(input("Me diga o terceiro lado? "))
        break
    except ValueError: print("Coloque apenas numeros.")

Soma = Lado1 + Lado2 + Lado3

print("Aqui está os lados em ordem", Lado1, ",", Lado2, ",", Lado3, ",", "e a soma de todos fica", Soma)
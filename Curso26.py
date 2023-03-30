import math

while True:
    try:
        ValorA = float(input("Me diga o valor do A? "))
        ValorB = float(input("Me diga o valor do B? "))
        ValorC = float(input("Me diga o valor do C? "))
        break
    except ValueError: print("Coloque apenas numeros!")

delta = ValorB ** 2 - 4 * ValorA * ValorC

if delta < 0:
    print("A equação, não possui raiz reais.")
elif delta == 0:
    print("A equação possui uma raiz reais x=", delta)
else:
    x1 = (-ValorB + math.sqrt(delta)) / (2 * ValorA)
    x2 = (-ValorB - math.sqrt(delta)) / (2 * ValorA)
    print("A equação possui duas raízes reais: x1 =",x1,"e x2 =",x2)
pi = 3.14
try:
    NumeroAoQuadrado = float(input("Quanto centimetros deseja calcular? "))
    NumeroAoQuadrado = NumeroAoQuadrado * NumeroAoQuadrado
    NumeroAoQuadrado = NumeroAoQuadrado * pi
except ValueError: print("Você não colocou somente numeros!")

try:
    print("Sua area calculada é de ", NumeroAoQuadrado, "cm² aproximadamente")
except NameError: print("Tente novamente.")
try:
    AreaQuadrado = float(input("Quantos cm tem o lado do quadrado ? "))
    AreaQuadrado = AreaQuadrado * AreaQuadrado
except ValueError: print("Você deve colocar numeros!")
try:
    print ("Seu quadrado tem a area de", AreaQuadrado, "cm²")
except NameError: print("Tente novamente.")
try:
    AreaQuadrado = AreaQuadrado * 2
except NameError: print(" ")
try:
    print("O dobro da area seria esse: ", AreaQuadrado, "cm²")
except NameError: print(" ")
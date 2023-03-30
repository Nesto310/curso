Vogal = input("Qual a letra que deseja verificar? ")
lista = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u",]
lista2 = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "x", "y", "w", "z"]

if Vogal in lista:
    print("Essa letra é uma vogal.")
elif Vogal in lista2:
    print("Essa letra é uma consoante")
else:
    print("Você deve colocar apenas 1 letra.")
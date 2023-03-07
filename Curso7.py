try:
    Metros = float(input("Quantos metros você tem? "))
except ValueError: print("Você deve colocar apenas numeros.")

Metros = int(Metros * 100)

print("Uau, você tem então ", Metros,"cm")
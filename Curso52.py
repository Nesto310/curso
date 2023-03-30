listanumero = []
while True:
    try:
        numero1 = float(input("Qual o primeiro numero? "))
        listanumero.append(numero1)
        numero2 = float(input("Qual o segundo numero? "))
        listanumero.append(numero2)
        numero3 = float(input("Qual o terceiro numero? "))
        listanumero.append(numero3)
        break
    except ValueError: print("Coloque apenas numeros.")

decrescente = sorted(listanumero, reverse=True)
print(f"O numero em ordem decrescente é:{decrescente}")
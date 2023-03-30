while True:
    try:
        produto1 = float(input("Qual o preço do primeiro produto? "))
        produto2 = float(input("Qual o preço do segundo produto? "))
        produto3 = float(input("Qual o preço do terceiro produto? "))
        break
    except ValueError: print("Coloque apenas numeros.")

if produto1 < produto2 and produto1 < produto3:
    print(f"Compre o primeiro produto, R${produto1} é o melhor preço")
elif produto2 < produto1 and produto2 < produto3:
    print(f"Compre o primeiro produto, R${produto2} é o melhor preço")
else:
    print(f"Compre o primeiro produto, R${produto3} é o melhor preço")
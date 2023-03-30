while True:
    try:
        Preco1 = float(input("Qual o preço do primeiro produto? "))
        Preco2 = float(input("Qual o preço do segundo produto? "))
        Preco3 = float(input("Qual o preço do terceiro produto? "))
        break
    except ValueError: print("Me apenas numeros!")

precos = [Preco1, Preco2, Preco3]

precosmenor = min(precos) #o min é representado como o menor

print("O melhor preço dos produto é", precosmenor)
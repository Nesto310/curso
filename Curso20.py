numeros = [] #lista
while True: # se o while estiver true, ele vai repetir o codigo caso acontecer um break
    try:
        numero = float(input("Me diga 1 numero ?"))
        numeros.append(numero) #vai usar a lista numeros, append, é para pegar tal coisa e adicionar na lista() tem que estra dentro da parentes
        numero2 = float(input("Me diga outro numero ?"))
        numeros.append(numero2)
        numero3 = float(input("Me diga mais um numero ?"))
        numeros.append(numero3)
        break #usado para não continuar o codigo, uma maneira de otimizar..
    except ValueError: print("Me diga apenas numeros")

numerosdecrescentes = sorted(numeros, reverse=True) #reverse é para fazer em ordem crescente ou decrescente (no caso está decrescente)
print("Os numeros em ordem decrescente são:", numerosdecrescentes)
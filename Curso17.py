while True:
    try:
        Nota1 = float(input("Qual a primeira nota ? ")) # repetição do programa até que o usuario faça a pergunta
        Nota2 = float(input("Qual a segunda nota ? ")) # corretamente
        break
    except ValueError: print("Apenas numeros.")



Media = Nota1 + Nota2
Media = Media / 2

print("A nota 1 é de ", Nota1, "nota 2 é de ", Nota2, "media dessa nota é de", Media)
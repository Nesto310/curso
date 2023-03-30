while True: 
    try:
        Nota1 = float(input("Qual foi a sua primeira nota bimestral? (Apenas numeros)"))
        Nota2 = float(input("Qual foi a sua segunda nota bimestral? (Apenas numeros)"))
        Nota3 = float(input("Qual foi a sua terceira nota bimestral? (Apenas numeros)"))
        Nota4 = float(input("Qual foi a sua quarta nota bimestral? (Apenas numeros)"))
        break
    except ValueError: print("Apenas numeros.")

Media = Nota1 + Nota2 + Nota3 + Nota4

Media = Media / 4

print(f"Sua media de nota foi de {Media}")
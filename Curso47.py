while True:  
    try:
        numerointeiro1 = int(input("Fale um numero inteiro."))
        numerointeiro2 = int(input("Fale um outro numero inteiro."))
        numeroreal = float(input("Fale um numero real."))
        break
    except ValueError: print("Você colocou letras, ou numeros real em lugar errado.")

soma = numerointeiro1 + numerointeiro2 + numeroreal

print(f"A soma total é de {soma}")
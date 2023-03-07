try:
    NumeroEscolher1 = int(input ("escolha um numero para somar: "))
except ValueError: print("Ops, parece que você não colocou só numero")
try:
    NumeroEscolher2 = int(input ("escolha outro numero para somar: "))
except ValueError: print("Ops, parece que você não colocou só numero")
try:
    NumeroSoma = int(NumeroEscolher1 + NumeroEscolher2)
    print ("A soma dos numeros é: ", NumeroSoma)
except ValueError: print("Você não colocou nas perguntas, os numeros.")

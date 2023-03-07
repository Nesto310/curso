numeroEscolhe = input("Escolhe algum numero: ")

try:
    numeroEscolhido = int(numeroEscolhe)
    print("Seu numero escolhido: ", numeroEscolhido)
except ValueError:
    print("Isso não é um numero valido!")
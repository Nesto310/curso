try:
    NumeroEscolher1 = int(input("Fale sua nota de matematica: "))
    
    NumeroEscolher2 = int(input("Fale sua nota de historia: "))
    
    NumeroEscolher3 = int(input("Fale sua nota de ingles: "))
    
    NumeroEscolher4 = int(input("Fale sua nota de portugues: "))
except ValueError: print("Você não colocou sua nota!, digite o numero, não letras")
Dividir = 4

try:
    NumeroMedia = NumeroEscolher1 + NumeroEscolher2 + NumeroEscolher3 + NumeroEscolher4
    NumeroMedia = NumeroMedia / Dividir
except NameError: print("Você não receberá sua media.")

try:
    print("Sua media é " , NumeroMedia)
except NameError: print("Concerte o seu erro na hora de colocar a nota!")
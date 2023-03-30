QualMes = int(input("Qual o mês ? (em numeros) "))
QualDia = int(input("Qual o dia do mês ? (em numeros) "))
QualAno = int(input("Qual o ano ? "))

Mes31 = [1, 3, 5, 7, 8, 10, 12]
validade = False
Mes30 = [4, 6, 9, 11]
Mesbisexto = [2]

if QualMes in Mes31:
    if QualDia <= 31:
        validade = True
elif QualMes in Mes30:
    if QualDia <= 30:
        validade = True
elif QualMes in Mesbisexto:
    if (QualAno % 4 == 0 and QualAno % 100 != 0) or (QualAno % 400 == 0):
        if(QualDia <= 29):
                valida = True
        elif(QualDia <= 28):
                valida = True

if validade == True:
    print("VALIDO")
else:
    print("Invalido.")
somaidades = 0 #quantidade somada das idades
media = 0 #media do grupo todo
idadevelho = 0 #esse vai guardar a idade do velho
nomevelho = "" #vai guardar o nome mais velho
totalmulher20 = 0 #vai pegar o total de mulheres com menos de 20 anos

for pessoa in range (1,5): #Pergunta 4 vezes a pessoa
  nome= str (input("Nome: ")) #nome
  idade= int (input("Idade: ")) #idade da pessoa
  sexo= str (input("Sexo [M/F]: ")) #sexo da pessoa
  somaidades = somaidades + idade #vai somar a idade com todas as idades que tem (idade do grupo)
  if pessoa == 1 and sexo == "M" : # se a pessoa == 1 for do sexo masculino
    idadevelho = idade #a idade velho vai ser igual a idade da pessoa
    nomevelho = nome #a pessoa mais velha vai pegar o nome de mais velho
  if sexo == "M" and idade > idadevelho : #se o sexo masculino e com idade maior que a idade velha
    idadevelho = idade #idade da pessoa que for mais velho que a outra, vai pegar o lugar de mais velho
    nomevelho = nome #a pessoa mais velha vai pegar o nome de mais velho
  if sexo == "F" and idade < 20: # se o sexo feminino e com idade menor que 20
    totalmulher20 = totalmulher20 + 1 #total de mulheres com menos de 20 anos somado + 1
media = somaidades / 4 #media vai ser igual a soma das idades divido por 4
print ("A média de idade do grupo é {}".format(media)) # vai pegar a media e mostrar
print ("O homem mais velho é {} e tem {} anos".format(nomevelho, idadevelho)) # vai pegar o mais velho
print ("Temos {} mulheres com menos de 20 anos.".format(totalmulher20))# e vai mostrar o total de pessoas novas
num = 5 
 
for i in range(num): 
    linha = '' 
    for j in range(i, -1, -1): 
        linha += '* ' 
 
    print(linha) 
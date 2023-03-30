num = 6 
for i in range(num): 
    linha = '' 
    for j in range(num): 
        if (i < num // 2 and j < num // 2) or (i >= num // 2 and j >= num // 2): 
            linha += '  ' 
        else: 
            linha += '* ' 
 
    print(linha)

 
  
num = 6 
for i in range(num): 
    linha = '' 
    for j in range(num): 
        if (i < num // 2 and j < num // 2) or (i >= num // 2 and j >= num // 2): 
            linha += '  ' 
        else: 
            linha += '* ' 
 
    print(linha) 

  
for i in reversed(range(1, num // 2)): 
    print('* ' * num) if i % 2 == 0 else print(' *' * num)
	    
num = 5 
 
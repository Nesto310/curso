achou = False 
i = 0 
frase = "clebao"

while (not achou) and (i < len(frase)): 
    if i % 2 == 0: 
        i += 1 
        continue 
 
    if frase[i] == ' ': 
        achou = True 
 
    i += 1 
print(f"{i}")
while True:
    try:
        numero = int(input("Digite um número inteiro menor que 1000: "))
        break
    except ValueError: print("Apenas nuemros inteiros.")

if numero >= 1000:
    print("Número inválido!")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10
    
    print(f"O número {numero} tem {centenas} centena(s), {dezenas} dezena(s) e {unidades} unidade(s).")
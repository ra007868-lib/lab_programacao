n_termos = int(input("Quantos termos da serie Fibonacci deseja ver? "))
a, b = 0,1  #mesma coisa de fazer separado
contador = 0
print("Sequência de Fibonacci")
while contador <= n_termos:
    print(a, end=", " if contador < n_termos else "")
    # Lógica de atualização F(n-1) + (n-2)
    proximo = a + b
    a = b
    b = proximo
    contador +=1 

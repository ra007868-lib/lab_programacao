num = int(input("Digite um numero interio positivo:"))
fatorial = 1
while num > 0:
    fatorial = fatorial * num
    num = num - 1
print("O Fatorila desse numero é: ", fatorial)
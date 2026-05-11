num = int(input("Digite um numero:"))
num_1 = int(input("Digite o segundo numero maior que o primeiro: "))
contador_pares = 0
soma = 0
while num <= num_1:
    if(num%2 == 0):
        contador_pares = contador_pares + 1
        soma = soma + num
    num = num + 1
print(contador_pares)
print("A soma é", soma)

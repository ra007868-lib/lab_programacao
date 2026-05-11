num = int(input("Digite um numero: "))
contador = 0
if num == 0:
    contador = 1
else:
    temp = num
    while temp > 0:
        temp //=10 #remove o ultimo digito
        contador += 1
print(f"O {num} possui {contador} digitos. ")
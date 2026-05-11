#Leia o peso e a altura
peso = float(input("Digite seu peso:(kg) "))
altura = float(input("Digite sua altura:(metros) "))
#1 Processamento
imc = peso/(altura**2)

if imc <=18.5:
    classificacao = "Abaixo do Peso"
elif imc <= 24.9:
    classificacao = "Saudável"
elif imc <=29.9:
    classificacao ="Peso em excesso"
elif imc <=34.9:
    classificacao="Obesidade grau I"
elif imc <=39.9:
    classificacao ="Obesidade grau II (severa)"
else:
    classificacao ="Obesidade grau III (mórbida)"

#Saída
print(" = " * 30) 
print(f"Seu IMC é: {imc: .2f}")
print(f"Classificação: {classificacao}")
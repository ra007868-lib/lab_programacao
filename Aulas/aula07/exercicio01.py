#Entrada
idade = int(input("Digite sua idade do atleta: "))
#Processamento
if idade < 5:
    categoria = "Sem categoria (muito jovem)"
elif idade <=7:
    categoria = "Infantil A"
elif idade <=11:
    categoria = "Infantil B"
elif idade <=17:
    categoria = "Juvenil"
else:
    categoria = "Adulto"

print(f"O atleta pertence à categoria: {categoria}")              

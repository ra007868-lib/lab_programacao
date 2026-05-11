#Entrada
porc_agua = float(input("Digite o nível da agua: "))
if porc_agua >= 90:
    nivel = "ALERTA: Nivel Crítico(Transbordando)!"
elif porc_agua >= 50:
    nivel = "Nível adequado."
elif porc_agua >= 1/20:
    nivel = "Nível Baixo(Atenção)."
else:
    nivel = "ALERTA: Reservatório Vazio!"

print(f"O tanque está no: {nivel}")


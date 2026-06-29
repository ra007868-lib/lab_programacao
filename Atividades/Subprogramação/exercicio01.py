def verificador_nota():
    entrada_nota = float(input("Digite sua nota: "))
    
    if entrada_nota > 6:
        print("Aprovado")
    elif entrada_nota > 4:
        print("Verificação Suplementar")
    else:
        print("Reprovado")
        
verificador_nota()
                
  
#for tabela in ("1","2","3","4","5","6","7","8","9","10"):
 #   for tabela2 in ("1","2","3","4","5","6","7","8","9","10"):
  #      resultado = [tabela * tabela2]
   #     if tabela != tabela2:
    #        print(tabela,'x', tabela2, "=",resultado)

# laço externo que percorre os numero de 1 a 10
for i in range(1,11):
#laço interno calcula a multiplicação
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")



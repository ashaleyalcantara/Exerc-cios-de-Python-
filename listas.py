listaO = []
listaP = []
listaI = []

for i in range(10):
    V = int(input("Digite o " + str(i) + "º número da lista: "))
    listaO.append(V)
    if V%2 == 0:
        listaP.append(V)
    else:
        listaI.append(V)
        
print("Lista completa", listaO)
print("Lista par", listaP)
print("Lista impar", listaI)

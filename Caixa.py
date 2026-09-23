
def CalcularTotal(lista):
    total = 0.0 
    for elementos in lista:
        total += elementos
    return total

def Desconto(total):
    if total>100:
        return total*0.90
    elif 50<total<=100:
        return total*0.95
    else:
        return total

lista = []  
while True:
    Valor = float(input("Digite um valor: "))
    if Valor == 0:
        break
    elif Valor<0:
        print("Valor inválido, digite novamente")
    else:
       lista.append(Valor)
total = CalcularTotal(lista)

print("O valor gasto foi de: R$", total)
print("O valor a ser pago é de: R$", Desconto(total))
print("Obrigada, volte sempre!!")



def maior(Lista):
    ma = Lista[0]
    for i in Lista:
        if i > ma:
            ma = i
    return ma

def menor(Lista):
    me = Lista[0]
    for i in Lista:
        if i < me:
            me = i
    return me


Lista = []


while True:
    valor = int(input("Digite um valor: "))
    if valor == 0:
        break
    Lista.append(valor)


print ("O maior número da lista é: ", maior(Lista))
print("O menor número da lista é:", menor(Lista))
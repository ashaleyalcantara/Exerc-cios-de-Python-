
def calcularmedia(notas):
    Media = notas/3
    return Media
def situacao(Media):
    if Media >= 7:
        return "Aprovado"
    elif 3<=Media<7:
        return "Recuperação" 
    else:
        return "Reprovado"
    
Nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))     
if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    print("Algum(s) dos valores digitados são inválidos, digite novamente") 
else:
    notas = n1 + n2 + n3  
    Media = calcularmedia(notas)
    print("Nome:", Nome)
    print("Média:", Media)
    print("Situação:", situacao(Media))
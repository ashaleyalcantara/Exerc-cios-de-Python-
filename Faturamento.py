def informacoesDeFaturamento(Lista):

    soma = 0
    for valor in Lista:
        soma += valor
    print("Total anual:", soma)

    media = soma / 12
    print("Média mensal:", media)

    maior = Lista[0]
    mes_maior = 0

    for indice, valor in enumerate(Lista):
        if valor > maior:
            maior = valor
            mes_maior = indice

    print("Maior faturamento:", maior)
    print("Mês do maior faturamento:", mes_maior + 1)  
    

FaturamentoAno = []

for i in range(12):
    valor = float(input(f"Digite o faturamento do mês {i+1}: "))
    FaturamentoAno.append(valor)

informacoesDeFaturamento(FaturamentoAno)

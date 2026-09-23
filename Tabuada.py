
N = int(input("Digite o número: "))
S = input("Digite o símbolo da operação (+, -, /, *): ")

if S == "+":
    for i in range(1, 11):
        print("O resultado de", i, "+", N, "é igual a", i + N)

elif S == "-":
    for i in range(1, 11):
        print("O resultado de", i, "-", N, "é igual a", i - N)

elif S == "/": 
        for i in range(1, 11):
            print("O resultado de", i, "/", N, "é igual a", i / N)

elif S == "*":
    for i in range(1, 11):
        print("O resultado de", i, "x", N, "é igual a", i * N)

else:
    print("Operação inválida! Use apenas +, -, / ou *.")


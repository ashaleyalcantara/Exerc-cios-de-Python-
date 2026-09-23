
while True:
  n1 = float(input("Digite o primeiro número: "))
  op = input("Digite o operador (+ - * /): ")      
  n2 = float(input("Digite o segundo número: "))
  if op == "+":
    resultado = n1 + n2
  elif op == "-":
    resultado = n1 - n2
  elif op == "*":
    resultado = n1 * n2
  elif op == "/":
    resultado = n1 / n2
  else:
    resultado = "Operador inválido!"
 
  print("Resultado:", resultado)

  C = input("Quer fazer outro cálculo (S/N)") 
 
  if C=="N":
     break
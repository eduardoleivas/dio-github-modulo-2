# Recebe do usuário os dados de entrada:
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Faz os cálculos das operações com os valores fornecidos e imprime o resultado
if operacao == '+':
  resultado = num1 + num2
elif operacao == '-':
  resultado = num1 - num2
elif operacao == '*':
  resultado = num1 * num2
elif operacao == '/':
  # Verifica se o segundo número não é zero para evitar divisão por zero
  if num2 != 0:
    resultado = num1 / num2
  else:
    resultado = "Erro: divisão por zero!"
else:
  resultado = "Operação inválida!"

print("Resultado:", resultado)

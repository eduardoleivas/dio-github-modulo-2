# Solicita ao usuário os dados de entrada
quantidade = int(input("Quantas vezes deseja imprimir a string? "))
texto = input("Digite a string que deseja imprimir: ")

# Itera 'quantidade' vezes para imprimir a string na tela
for _ in range(quantidade):
    print(texto)

# Inicializa uma lista vazia para armazenar os números inseridos pelo usuário
numeros = []

# Inicia um loop infinito para coletar números do usuário
while True:
    # Solicita que o usuário digite um número e o converte para o tipo float
    numero = float(input("Digite um número: "))

    # Verifica se o número é negativo
    if numero < 0:
        # Exibe uma mensagem indicando que o número é negativo e interrompe o loop
        print("O número é negativo")
        break
    else:
        # Adiciona o número positivo à lista
        numeros.append(numero)    

    # Exibe a lista atualizada contendo os números inseridos até o momento      
    print(numeros)
    


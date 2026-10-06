def calculadora():
    # Mensagem de boas-vindas
    print("Bem-vindo à Calculadora de Operações Básicas!")

    # Mostrar as opções disponíveis
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Receber a escolha do usuário
    escolha = input("Digite o número da operação: ")

    # Receber os números para o cálculo
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Verificar qual operação foi escolhida e calcular
    if escolha == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif escolha == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif escolha == "3":
        print(f"Resultado: {num1} * {num2} = {num1 * num2}")
    elif escolha == "4":
        if num2 != 0:
            print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("Erro: divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

# Executar o programa
calculadora()

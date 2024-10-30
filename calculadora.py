def calcular():

    print("Selecione a operação:")
    print("0. sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite o número da operação (1/2/3/4) para encerrar: ")
                
        if escolha == '0':
            break

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")

            elif escolha == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")

            elif escolha == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")

            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")

            else:
                print("Escolha inválida!")

if __name__ == "__main__":
    calcular()

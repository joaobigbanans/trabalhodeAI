MAX_HISTORICO = 5

def inputint(text):
    print(text)
    while True:
        try:
            return int(input())
        except ValueError:
            print("Valor não numerico. Introduza novamente")

def adicionaAoHistorico(historico, text):
    if len(historico) == MAX_HISTORICO:
        del historico[0]

    historico.append(text)

def mostraHistorico(historico):
    if len(historico) == 0:
        print("Histórico vazio.")

def calcular():

    print("Selecione a operação:")
    print("0. sair")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Histórico")

    while True:
        escolha = input("Digite o número da operação (1/2/3/4/5) para encerrar: ")
                
        if escolha == '0':
            break
        
        elif escolha == '5':
            if len(historico) == 0:
                print("Histórico vazio.")
            else:
                print("Histórico de operações")
                for operacao in historico:
                    print(operacao)

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")
                adicionaAoHistorico(historico, f"{num1} + {num2} = {resultado}")

            elif escolha == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")
                adicionaAoHistorico(historico, f"{num1} - {num2} = {resultado}")
                
            elif escolha == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")
                adicionaAoHistorico(historico, f"{num1} * {num2} = {resultado}")

            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")
                    adicionaAoHistorico(historico, f"{num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")

            else:
                print("Escolha inválida!")

if __name__ == "__main__":
    calcular()

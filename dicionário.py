#função para o dicionário
stand = {
    "carro1" : {"nome": "mercedes", "preço": 80000, "quantidade": 4},
    "carro2" : {"nome": "porsche 911 carrera", "preço": 160000, "quantidade": 2},
    "carro3" : {"nome": "honda civic", "preço": 9000, "quantidade": 8},
    "carro4" : {"nome": "renout zoe", "preço": 45000, "quantidade": 5},
    "carro5" : {"nome": "citroen ami", "preço": 7600, "quantidade": 11}
}

def print_stand():
    print("Produtos disponiveis no stand:")
    for x, y in stand.items():
        print(f"{x}: Nome: {y["nome"]}, Preço: {y["preço"]:.2f}, Quantidae: {y["quantidade"]} unidades.")

stand["carro2"] = {"nome": "porsche 911 carrera","preço": 140000,"quantidade": 4}

stand["carro2"] = {"nome": "porsche 911 carrera","preço": 140000,"quantidade": 4}

def quant_prod(cod_prod):
    qtd_produto = stand[cod_prod]["quantidade"]
    print("O total de " + stand[cod_prod]["nome"] + " do stand é: ", qtd_produto)

def quat_total():
    total =0
    for produto in stand.values():
       total += produto["quantidade"]
    print(f"Numero total de carros no stand: {total} ")

def vender_produto(cod_prod, quantidade):
    if cod_prod in stand:
        produto = stand[cod_prod]
        if produto["quantidade"] >= quantidade:
            produto["quantidade"] -= quantidade
            print(f"Venda realizada. {quantidade} unidade de {produto["nome"]} vendidas.")
        else:
            print(f"Estoque insuficiente para {produto["nome"]}. Apenas {produto["quantidade"]} unidades disponiveis.")
    else:
        print("Codigo de produto invalido.")

def adicionar_produto(cod_prod, nome, preco, quantidade):
    if cod_prod in stand:
        print("Já existe um carro com este código. Atualizando os valores...")
    stand[cod_prod] = {"nome": nome, "preço": preco, "quantidade": quantidade}
    print(f"Produto '{nome}' adicionado/atualizado com sucesso!")

def menu():
    while True:
        print("\n=== MENU DO STAND ===")
        print("1. Ver carros do stand")
        print("2. Comprar carros")
        print("3. Adicionar carros")
        print("4. quantidade total de carros")
        print("5. Sair do stand")
        opcao = input("Escolha uma opção (1-4): ")

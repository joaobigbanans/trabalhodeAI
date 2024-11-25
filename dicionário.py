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

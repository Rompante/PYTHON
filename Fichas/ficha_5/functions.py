#3. Crie uma função que receba o nome do produto, o preço e o iva e guarde a 
#informação em um dicionário onde as chaves serão product, price e tax. 
# A função deve ser denominada add.

def add(product, price, tax = 0.23):
    return {
        "produto": product,
        "preço": price,
        "iva": tax
    }

def update_final_price(d):
    d["final_price"] = d["price"] * (1 + d["iva"])

def print_product(d):
    return f"Produto: {d['produto']} com Preço de {d['price']} e IVA {d['tax']*100}% com Preço final de {d['final_price']}"


def menu():
    print("\n========================================")
    print("          SISTEMA DE PRODUTOS           ")
    print("========================================")
    print("1. Inserir um novo produto")
    print("2. Listar os produtos existentes")
    print("3. Atualizar o preço final de todos os produtos existentes na lista")
    print("4. Imprimir os dados de um produto específico")
    print("5. Terminar a aplicação")
    print("========================================\n")

    op = int(input("Escolha a opção: "))

    return op
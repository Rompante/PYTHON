#2. Crie uma lista vazia denominada products.
products = []

#3. Crie uma função que receba o nome do produto, o preço e o iva e guarde informação em um dicionário onde as chaves serão product, price e tax. A função deve ser denominada add.
def add(product, price, tax = 0.23):
    produto = {
        "produto": product,
        "preço": price,
        "iva": tax
    }
    products.append(produto)

add("Computador", 1000)
print(products)

def update_final_price(added_product):
    final_price = (price * (1+tax))
    
import os
from Fichas.ficha_5.functions import add, update_final_price, print_product, menu

#2. Crie uma lista vazia denominada products.
products = []

# products.append(add("camisa", 12.23, 0.13))

# prd = input("Digite o nome do produto: ")
# pri = float(input("Digite o preço do produto: "))
# iva = float(input("Digite o iva do produto: "))

# products.append(add(prd, pri, iva))
# update_final_price(products[0])

# for product in products:
#     print(print_product(products))

escolha = menu()

while True:
    match (escolha):
        case 1:
            prd = input("Digite o nome do produto: ")
            pri = float(input("Digite o preço do produto: "))
            iva = float(input("Digite o iva do produto: "))
            products.append(add(prd,float(pri), float(iva)))
        case 2:
            # Listar os produtos existentes
            for product in products:
                if "final_price" in product.keys():
                    update_final_price(product)
            print(print_product(products))
            x = input("Prima uma tecla para continuar...")
        case 3:
            # Atualizar o preço final de todos os produtos existentes na lista
            for product in products:
                update_final_price(product)
        case 4:
            # Imprimir os dados de um produto específico
            encontrei = False
            pesquisa = input("Digite o nome do produto: ")
            for p in products:
                if p["produto"] == pesquisa:
                    print(print_product(p))
                    encontrei = True
            if not encontrei:
                print("este produto não faz parte da lista!")
            x = input("Prima uma tecla para continuar...")
        case 5:
            break
    os.system("cls")
    escolha = menu()

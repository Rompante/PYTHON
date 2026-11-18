# 2. Modularização (Funções)

# Todo o código deve ser organizado em funções bem definidas, cada uma responsá-
# vel por uma única tarefa.

# 3. Operações de Gestão (Menu Principal)
# ▪ Ver inventário: Exibir todos os itens do inventário de forma clara e formatada
# (ex: em formato de tabela). Se o inventário estiver vazio, exibir uma mensagem
# apropriada.
# ▪ Adicionar Item: Solicitar ao utilizador o título, autor, quantidade e preço do
# novo livro.
# o Gerar automaticamente um novo id único (o maior ID existente + 1).
# o Criar o dicionário do novo item e adicioná-lo à lista de inventário.
# ▪ Atualizar Stock: Solicitar ao utilizador o id do item a ser modificado. Se o item
# for encontrado, solicitar a nova quantidade em stock. Atualizar o valor da chave
# quantidade no dicionário correspondente
# ▪ Remover Item: Solicitar ao utilizador o id do item a ser removido. Remover o
# dicionário correspondente da lista de inventário.
# ▪ Pesquisa Avançada: Pesquisar itens por titulo ou autor.
# ▪ Relatório de Stock: Implementar uma função que calcule e exiba o valor total
# do inventário

def menu():
    print("\n========================================")
    print("          SISTEMA DE INVENTÁRIO         ")
    print("========================================")
    print("1. Ver inventário")
    print("2. Adicionar Item")
    print("3. Atualizar Stock")
    print("4. Remover Item")
    print("5. Pesquisa Avançada")
    print("6. Relatório de Stock")
    print("7. Terminar a aplicação")
    print("========================================\n")

    op = int(input("Escolha a opção: "))

    return op

def ver_inventario(inventario):
    if not inventario:
        print("O inventário está vazio.")
        return

    colunas = ("ID", "Título", "Autor", "Quantidade", "Preço")
    linhas = [
        (
            str(item["id"]),
            item["titulo"],
            item["autor"],
            str(item["quantidade"]),
            f"{item['preco']:.2f}",
        )
        for item in inventario
    ]
    larguras = [
        max(len(colunas[indice]), *(len(linha[indice]) for linha in linhas))
        for indice in range(len(colunas))
    ]
    formato = " | ".join(f"{{:<{largura}}}" for largura in larguras)

    print(formato.format(*colunas))
    print("-+-".join("-" * largura for largura in larguras))
    for linha in linhas:
        print(formato.format(*linha))


def adicionar_item(inventario):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    quantidade = int(input("Digite a quantidade em stock: "))
    preco = float(input("Digite o preço unitário: "))
    novo_id = max((item["id"] for item in inventario), default=0) + 1
    inventario.append({
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco,
    })
    print(f"Livro adicionado com sucesso. ID: {novo_id}.")


def atualizar_stock(id_pesquisa, inventario):
    item_encontrado = next(
        (item for item in inventario if item["id"] == id_pesquisa),
        None,
    )
    if item_encontrado is None:
        print("Livro não encontrado.")
        return

    item_encontrado["quantidade"] = int(
        input("Digite a nova quantidade em stock: ")
    )
    print(f"Livro com ID {id_pesquisa} atualizado com sucesso.")


def remover_item(id_remover, inventario):
    item_encontrado = next(
        (item for item in inventario if item["id"] == id_remover),
        None,
    )
    if item_encontrado is None:
        print("Livro não encontrado.")
        return

    inventario.remove(item_encontrado)
    print("Livro removido com sucesso.")


def pesquisa_avancada(inventario):
    pesquisa = input("Digite o título ou autor a pesquisar: ").strip().casefold()
    resultados = [
        item
        for item in inventario
        if pesquisa in item["titulo"].casefold()
        or pesquisa in item["autor"].casefold()
    ]
    if not resultados:
        print("Nenhum livro encontrado.")
        return

    ver_inventario(resultados)


def relatorio_stock(inventario):
    valor_total = sum(
        item["quantidade"] * item["preco"]
        for item in inventario
    )
    print(f"Valor total do inventário: {valor_total:.2f}")
    return valor_total

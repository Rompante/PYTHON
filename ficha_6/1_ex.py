# 1. Estrutura de Dados (Listas e Dicionários)

# A. Item de Inventário: Cada livro no inventário deve ser representado por um dici-
# onário com as seguintes chaves:

# ▪ id (Inteiro único)
# ▪ titulo (String)
# ▪ autor (String)
# ▪ quantidade (Inteiro, número de unidades em stock)
# ▪ preco (Float, preço unitário)

# B. Inventário Total: O inventário completo deve ser armazenado numa lista de dici-
# onários.
from functions import menu


livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "quantidade": 5,
        "preco": 39.99
    },
    {
        "id": 2,
        "titulo": "Figueiredo e o Corvo",
        "autor": "George Orwell",
        "quantidade": 8,
        "preco": 29.99
    },
    {
        "id": 3,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "quantidade": 12,
        "preco": 19.99
    }
]

# 2. Modularização (Funções)

# Todo o código deve ser organizado em funções bem definidas, cada uma responsá-
# vel por uma única tarefa.

escolha = menu()

while True:
    match (escolha):
        case 1:
            # Ver inventário
            if not livros:
                print("O inventário está vazio.")
            else:
                print("Inventário:")
                for livro in livros:
                    print(f"ID: {livro['id']}, Título: {livro['titulo']}, Autor: {livro['autor']}, Quantidade: {livro['quantidade']}, Preço: {livro['preco']}")
            x = input("Prima uma tecla para continuar...")
        case 2:
            # Adicionar Item
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            quantidade = int(input("Digite a quantidade em stock: "))
            preco = float(input("Digite o preço unitário: "))
            novo_id = max([livro["id"] for livro in livros], default=0) + 1
            novo_livro = {
                "id": novo_id,
                "titulo": titulo,
                "autor": autor,
                "quantidade": quantidade,
                "preco": preco
            }
            livros.append(novo_livro)
        case 3:
            # Atualizar Stock

            # Pede ao utilizador o ID do livro que pretende modificar
            # O int() converte o valor introduzido para um número inteiro
            id_atualizar = int(input("Digite o ID do livro a ser modificado: "))

            # Percorre a lista de livros e procura aquele cujo ID corresponde ao introduzido
            # Se encontrar, guarda o livro na variável livro_encontrado
            # Se não encontrar nenhum livro, guarda None
            livro_encontrado = next((livro for livro in livros if livro["id"] == id_atualizar), None)

            # Verifica se o livro foi encontrado
            if livro_encontrado:

                # Pede ao utilizador a nova quantidade de stock
                # Converte o valor introduzido para um número inteiro
                nova_quantidade = int(input("Digite a nova quantidade em stock: "))

                # Acede à chave "quantidade" do livro encontrado
                # Substitui a quantidade antiga pela nova quantidade introduzida
                livro_encontrado["quantidade"] = nova_quantidade

                # Informa o utilizador de que a atualização foi realizada com sucesso imprime o id do livro atualizado
                print(f"Livro com ID {id_atualizar} atualizado com sucesso.")

            # Caso o livro não seja encontrado
            else:

                # Informa o utilizador de que o livro não existe
                print("Livro não encontrado.")

        case 4:
            # Remover Item

            # Pede ao utilizador o ID do livro que pretende remover
            id_remover = int(input("Digite o ID do livro a ser removido: "))

            # Percorre a lista de livros e procura aquele cujo ID corresponde ao introduzido
            livro_encontrado = next((livro for livro in livros if livro["id"] == id_remover), None)

            # Verifica se o livro foi encontrado
            if livro_encontrado:

                # Remove o livro da lista de livros
                livros.remove(livro_encontrado)

                # Informa o utilizador de que a remoção foi realizada com sucesso
                print("Livro removido com sucesso.")

            # Caso o livro não seja encontrado
            else:

                # Informa o utilizador de que o livro não existe
                print("Livro não encontrado.")
        case 5:
            ...
        case 6:
            ...
        case 7:
            break
    escolha = menu()


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
from functions import (
    adicionar_item,
    atualizar_stock,
    menu,
    pesquisa_avancada,
    relatorio_stock,
    remover_item,
    ver_inventario,
)


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
            ver_inventario(livros)
        case 2:
            adicionar_item(livros)
        case 3:
            id_atualizar = int(input("Digite o ID do livro a ser modificado: "))
            atualizar_stock(id_atualizar, livros)
        case 4:
            id_remover = int(input("Digite o ID do livro a ser removido: "))
            remover_item(id_remover, livros)
        case 5:
            pesquisa_avancada(livros)
        case 6:
            relatorio_stock(livros)
        case 7:
            break
    escolha = menu()


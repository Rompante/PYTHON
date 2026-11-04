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
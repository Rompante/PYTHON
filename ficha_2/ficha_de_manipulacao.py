import random

tarefas = ["T1", "T2", "T3"]

# Inserir uma tarefa
tarefas.append("T4") 
print(f"Lista após append: ", tarefas)

# INSERIR VÁRIAS
tarefas.extend(["T4", "T5"])
print(f"Lista após extend: ", tarefas)

# INSERIR TAREFA EM POSIÇÃO ESPECÍFICA
tarefas.insert(2, "T6") 
print(f"Lista após insert: ", tarefas)

# REMOVER TAREFA POR NOME
tarefas.remove("T1")
print(f"Lista após remove: ", tarefas)

# REMOVER O ÚLTIMO ELEMENTO
tarefas.pop()
print(f"Lista após pop: ", tarefas)

# CONTAR OCORRÊNCIAS DA TAREFA
y = len(tarefas)
print(f"Número total de tarefas (tamanho da lista): {y}")

# ENCONTRAR ÍNDICE DE TAREFAS
indice = tarefas.index("T6")
print(f"Índice da primeira ocorrência de 'T6': {indice}")

# Ordenar Tarefas:
tarefas.sort()
print(f"Lista ordenada alfabeticamente: ", tarefas)

# Inverter Ordem das Tarefas:
tarefas.reverse()
print(f"Lista com ordem invertida: ", tarefas)

# Copiar Lista de Tarefas:
copia_tarefas = tarefas.copy()
print("Cópia independente da lista: ", copia_tarefas)

# REMOVER TODAS AS TAREFAS
tarefas.clear()
print(f"Lista após clear (vazia): ", tarefas)
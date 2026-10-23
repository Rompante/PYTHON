aluno = {
    "nome": "Carlos",
    "idade":17,
    "cidade":"Famalicão",
    "disciplina": ["Matematica", "Pogramação", "Ingles"]
    }
# print(aluno["nome"])

#Alterar valor de uma chave 
aluno["idade"] = 18
#inserir uma nova chave
aluno["estado_civil"] = "Solteiro"
# print(aluno)
#Imprimir as caracteristicas do aluno
for chave in aluno.keys():
    print(f"{chave}", end="")

#Imprimir somente os valores
print() 
for valor in aluno.values():
    print(f"{valor}", end="")

#Imprimir a chave e valor
print()
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
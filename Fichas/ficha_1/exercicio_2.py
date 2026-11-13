import random

notas = []

for i in range(15):
    notas.append(random.randint(0, 20))

print("Lista completa:", notas)

soma = sum (notas)
maior = max(notas)
menor = min(notas)
media = soma / len(notas)

aprovado = 0
reprovado = 0
superior = 0

for n in notas:
    if n >= 10:
        aprovado += 1
    else:
        reprovado += 1
    
    if n >= 16:
            superior += 1


print("numero de aprovado: ", aprovado)
print("numero de reprovado: ", reprovado)
print("Quantos tiveram nota igual ou superior a 16? ", superior)
print("media: ", media)
print("maior: ", maior)
print("menor: ", menor)

prec_aprovados= (aprovado / len(notas)) * 100
print(f"Percentagem de aprovados: {round(prec_aprovados,2)}")
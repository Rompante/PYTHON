import random

numeros = []

for i in range(30):
    numeros.append(random.randint(1, 100))

print("Lista completa:", numeros)


soma = sum (numeros)
maior = max(numeros)
menor = min(numeros)
media = soma / len(numeros)

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

numeros_superiores_media = [n for n in numeros if n > media]
quantidade_superiores = len(numeros_superiores_media)



print("numero de pares: ", pares)
print("numero de pares: ", impares)
print("media: ", media)
print("maior: ", maior)
print("menor: ", menor)
print("Quantidade de numeros acima da media: ", quantidade_superiores)
print("Numeros acima da media : ", numeros_superiores_media)

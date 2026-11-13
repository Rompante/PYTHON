nums = [2,5,8,11,9,13]

soma = sum (nums)
maior = max(nums)
menor = min(nums)
media = soma / len(nums)


# # imprimir a lista
# print(nums)
# # imprimir um elemento da lista
# print(nums[2]) #8
# # inserir um novo elemento no final da lista
# nums.append(17)
# #inserir varios elementos no final da lista 
# nums.append([12,16])
# # Inserir em posição especifica
# nums.insert(3,29)



# #Remover o elemento no final da lista
# nums.pop()
# # Remover um elemento de uma posição especifica da lista pelo indice
# nums.pop(2)
# #Remover um elemento de uma posição especifica da lista pelo o valor
# nums.remove(17)
# #nº de elementos da lista 
# total = len(nums)

# for n in nums: # Para cada elemento da minha lista
#     if n <= 10:
#         print(n, end=" ")
# for indice in range(len(nums)):
#     if nums[indice] <= 10:
#         print(nums[indice], end=" ")

#copiar uma lista 

jogadores =  ["J1","J2","J3"]

# Inserir um jogador
jogadores.append("J4") # ["J1","J2","J3","J4"]

# Inserir vários
jogadores.extend(["J5","J6"]) # ["J1","J2","J3","J4","J5","J6"]

nj = ["J7","J8"] # ["J1","J2","J3","J4","J5","J6","J7","J8"]
jogadores.extend(nj)

#Inserir um em uma posição específica
jogadores.insert(2,"J9") # ["J1","J2","J9","J3","J4","J5","J6","J7","J8"]

# Remover o último jogador
jogadores.pop() # ["J1","J2","J9","J3","J4","J5","J6","J7"]

# Remover um jogador em uma posição específica
jogadores.pop(4) # ["J1","J2","J9","J3","J5","J6","J7"]

# Remover o jogador pelo nome
jogadores.remove("J6") # ["J1","J2","J9","J3","J5","J7"]

# Saber o nº de jogadores
y = len(jogadores) # 6

# Copiar uma lista
lista1 = [1,2,3]
lista2 = lista1 # As listas ficam ligadas
print(lista1,lista2)
lista1.append(5)
print(lista1,lista2)
lista3 = lista1.copy() # As listas são independentes
lista1.append(7)
print(lista1, lista2, lista3)

# Ordenar
lista1.sort()

# Ordenar descendentemente
lista1.sort(reverse=True)

# Inverter a lista
lista1.reverse()

# Devolver o indice de um element ´
jogadores.index("J3") # 3

# ["J1","J2","J9","J3","J5","J7"]
jogadores.append("J5")

#Nº de ocorrêncas do J5
jogadores.count("J5")

# LIST COMPREHENSION
nums = [i for i in range(1,101)]
print(nums)

nums2 = [8,11,5,3,21,19,14,7]
# nums_filtrados = []
# for num in nums2:
#     if 10 <= num <= 20:
#         nums_filtrados.append(num)

nums_filtrados = [num for num in nums2 if 10 <= num <= 20]

nums_filtrados2 = []
for num in nums2:
    if 10 <= num <= 20:
        if num % 2 == 0: # é par
            nums_filtrados2.append(num*2)
        else:
            nums_filtrados2.append(num)

# [11,28,19]
nums_filtrados3 = [num*2 if num % 2 else num for num in nums2 if 10 <= num <= 20]

print(nums_filtrados3)

frutas = ["morango", "banana" , "ameixa", "pera"]
# Nº de caracteres de cada fruta
lestras_frutas = [len (fruta) for fruta in frutas ]
print(lestras_frutas)

nome = "marcelo"
print(nome)
nome = list(nome)
print(nome)
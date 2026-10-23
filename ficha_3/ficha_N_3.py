# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# pares = [num for num in nums if num % 2 == 0]
# quadrados = [num*num for num in nums]
# maior = [num for num in nums if num > 5]
# print(pares, quadrados, maior)

# frutas = ["morango", "banana" , "ameixa", "pera"]
# # Nº de caracteres de cada fruta
# lestras_frutas = [len (fruta) for fruta in frutas ]
# print(lestras_frutas)

#nome = 'MarcelO ViEiRaamorIM'


# 1. Lista com os números pares de 1 a 10
pares = [n for n in range(1, 11) if n % 2 == 0]
print("1. Números pares:", pares)


# 2. Lista com os quadrados dos números de 1 a 10
quadrados = [n**2 for n in range(1, 11)]
print("2. Quadrados:", quadrados)


# 3. Lista com o tamanho de cada palavra
palavras = ["Python", "Olá", "Computador", "Casa"]
tamanhos = [len(palavra) for palavra in palavras]
print("3. Tamanho das palavras:", tamanhos)


# 4. Lista apenas com os números maiores que 5
numeros = [2, 7, 4, 9, 1, 6, 10]
maiores = [n for n in numeros if n > 5]
print("4. Números maiores que 5:", maiores)


# 5. Lista com as letras maiúsculas de uma string
nome = "MarcelO ViEiRa amorIM"
maiusculas = [letra for letra in nome if letra.isupper()]
print("5. Letras maiúsculas:", maiusculas)


# 6. Dobro dos múltiplos de 3; os restantes ficam iguais
numeros = [1, 3, 5, 6, 8, 9, 10, 12]
resultado = [n * 2 if n % 3 == 0 else n for n in numeros]
print("6. Resultado:", resultado)


# 7. Nomes que começam por A, em maiúsculas
nomes = ["Ana", "Pedro", "António", "Maria", "André"]
resultado = [nome.upper() for nome in nomes if nome.upper().startswith("A")]
print("7. Nomes começados por A:", resultado)


# 8. Comprimento das frutas com mais de 5 letras; caso contrário, 0
frutas = ["banana", "pera", "laranja", "uva", "morango", "maçã"]
resultado = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print("8. Comprimento das frutas:", resultado)

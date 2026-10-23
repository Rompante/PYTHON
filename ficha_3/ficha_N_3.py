lista = [1,2,3,4,5,6,7,8,9,10]

# pares = [num for num in lista if num % 2 == 0]
# quadrados = [num*num for num in lista]
# maior = [num for num in lista if num > 5]
# print(pares, quadrados, maior)

# frutas = ["morango", "banana" , "ameixa", "pera"]
# # Nº de caracteres de cada fruta
# lestras_frutas = [len (fruta) for fruta in frutas ]
# print(lestras_frutas)

# nome = 'MarcelO ViEiRaamorIM'


# 1. Lista com os números pares de 1 a 10
pares = [nums for nums in lista if nums % 2 == 0]
print("1. Números pares:", pares)


# 2. Lista com os quadrados dos números
quadrados = [nums*nums for nums in lista]
print("2. Quadrados:", quadrados)


# 3. Lista com o tamanho de cada palavra
frutas = ["morango", "banana" , "ameixa", "pera"]
letras_frutas = [len (fruta) for fruta in frutas ]
print("3. Tamanho das palavras:", letras_frutas)


# 4. Lista apenas com os números maiores que 5
maiores = [nums for nums in lista if nums > 5]
print("4. Números maiores que 5:", maiores)

# 5 
nome = "MarcElO ViEiRa amorIm"
maiusculas = [letra for letra in nome if letra.isupper()] # se a letra for Maiuscula Adiciona a lsita senão nao adiciona como fosse true ou false o isupper()
print("5. Letras maiúsculas:", maiusculas)

# 6 multiplos de 3
resultado = [nums * nums if nums % 3 == 0 else nums for nums in lista]
print("6. Resultado:", resultado)

# 7. Nomes que começam por A, em maiúsculas
nomes = ["Ana", "Pedro", "António", "Maria", "André"]
resultado = [nome.upper() for nome in nomes if nome.upper().startswith("A")]
print("7. Nomes começados por A:", resultado)


# 8. Comprimento das frutas com mais de 5 letras; caso contrário, 0
frutas = ["banana", "pera", "laranja", "uva", "morango", "maçã"]
resultado = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas] # se a palavra for acima de 5 aparece o tamanho de letras senao so aparece o zero 
print("8. Comprimento das frutas:", resultado)
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

pares = [num for num in nums if num % 2 == 0]
quadrados = [num*num for num in nums]
maior = [num for num in nums if num > 5]
print(pares, quadrados, maior)

frutas = ["morango", "banana" , "ameixa", "pera"]
# Nº de caracteres de cada fruta
lestras_frutas = [len (fruta) for fruta in frutas ]
print(lestras_frutas)

nome = 'MarcelO ViEiRaamorIM'
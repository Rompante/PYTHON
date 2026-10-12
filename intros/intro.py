# num1 = 5
# x = str(num1)

# Tipos de dados: str,int,float,bool,list,dict,tuple,set
"""
Comentarios
sgsygsai
ssoij
"""

# print(num1, end= " ")
# num2: int = 8
# print(num2)
# num1 = "Marcelo"
# print(type(num1))

n1 = int(input ("Insira o primeiro Valor: "))
n2 = int(input ("Insira o segundo Valor: "))
s = n1 + n2
print(f"A soma de {n1} com {n2} é igual a {s}")

# Operadores aritemetricos: +, -, *, /, %, \(divisao inteira)
# Operadores de comparação: >, <, <=, >=, ==, !=
# Operadores lógicos: and, or, not

# ativo = True
# if ativo: False

nums = [2,8,11,7,15]
nums.append(5) # [2,8,11,7,15]
# Adicionar varios elementos a lista
nums.extend([1,4,7]) # [2,8,11,7,15,5,1,4,7]
# Adicionar um elemento em uma posição específica da lista
nums.insert(2,23) # [2,8,23,11,7,15,5,1,4,7]
# Remover numero 15
nums.remove(15)
print(nums)

# if num1 > 3:
#     print("O numero é maior que 3")    
#     print("Dentro do if")  
# print("Fora do if")  
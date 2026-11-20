class Cliente:
    #Atributos da classe
    total_clientes = 0

    def __init__(self, nome, idade, altura):
        #Atributos da instancia
        self.nome = nome
        self.idade = idade
        self.altura = altura
        Cliente.total_clientes += 1
    # Metodos especiais - dunder methods
    def __str__(self):
        return f"Cliente: {self.nome}, Idade: {self.idade}, Altura: {self.altura}"
    def __eq__(self, c1):
        return self.nome == c1.nome
    
    
c1 = Cliente("Ana", 62, 1.75)
c2 = Cliente("Maria", 35, 1.80)
c3 = Cliente("Maria", 60, 1.70)

if c1 == c2:
    print("ok")
if c2 == c3:
    print("segundo ok")

print(f"Total de clientes: {Cliente.total_clientes}")
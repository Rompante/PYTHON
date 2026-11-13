biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}


for livro in biblioteca.values():
    if livro["disponivel"]:
        print(livro["titulo"])


biblioteca["livro4"] = {
    "titulo": "I love APPLES",
    "autor": "AJ Figueiredo",
    "ano": 2067,
    "disponivel": True
}


biblioteca["livro1"]["disponivel"] = False

Luciano_Ramalho = {}
for livro in biblioteca.values():
    if livro["autor"] == "Luciano Ramalho":
        Luciano_Ramalho[livro["titulo"]] = livro



print(biblioteca)
print(Luciano_Ramalho)
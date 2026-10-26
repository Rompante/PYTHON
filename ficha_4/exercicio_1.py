aluno = {
     "aluno1": {
        "nome": "Ana Silva",
        "idade": 17,
        "cidade": "Porto",
        "curso": "Programador",
        "Disciplinas": {
            "Matemática",
            "Física",
            "Informática"
        },
        "Notas": {
            "Matemática": 18,
            "Física": 17,
            "Informática": 19
        }
    }
}


# Adicionar a nova disciplina e a respetiva nota
aluno["aluno1"]["Disciplinas"].add("Português")
aluno["aluno1"]["Notas"]["Português"] = 16
aluno["aluno1"]["idade"] = 18

print(aluno["aluno1"])

media_nota_alunos = 0.0
soma_notas = 0.0

for aluno in aluno.values():
    nome_aluno = aluno["nome"]
    notas_aluno = []
    for nota in aluno["Notas"].values():
        notas_aluno.append(nota)

media_nota_alunos = round(sum(notas_aluno) / len(notas_aluno), 2)
print(f"Aluno(a) {nome_aluno} teve Média de {media_nota_alunos} valores")


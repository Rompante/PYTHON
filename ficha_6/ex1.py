import random

# Constantes do jogo
VIDA_MAXIMA_POCAO = 300   # a poção nunca ultrapassa os 300 pontos de vida
CURA_POCAO = 25           # pontos de vida recuperados por poção


def criar_jogador():
    # Dicionário com os dados do jogador
    return {
        "vida": 300,
        "ataque": 20,
        "pocoes": 2,
        "pontos": 0
    }


def criar_inimigos():
    # Lista de dicionários com os tipos de inimigo
    tipos = [
        {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
        {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
        {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
        {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
        {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500}
    ]

    # Seleciona aleatoriamente entre 3 e 5 inimigos
    quantidade = random.randint(3, 5)
    inimigos = []
    for _ in range(quantidade):
        # dict() faz uma cópia, para cada inimigo ter a sua própria vida
        inimigos.append(dict(random.choice(tipos)))
    return inimigos


def titulo():
    print("========================================")
    print("          BATALHA DE INIMIGOS           ")
    print("========================================")


def menu():
    print("\n========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")

    try:
        op = int(input("Escolha a opção: "))
    except ValueError:
        # Se não for um número devolve 0 (opção inexistente)
        op = 0
    return op


def inimigos_vivos(inimigos):
    # Devolve só os inimigos com vida acima de zero
    return [inimigo for inimigo in inimigos if inimigo["vida"] > 0]


def listar_inimigos(inimigos):
    vivos = inimigos_vivos(inimigos)
    if not vivos:
        print("Não existem inimigos vivos.")
        return
    print("\nInimigos vivos:")
    for i, inimigo in enumerate(vivos, start=1):
        print(f"{i} - {inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")


def atacar_inimigo(jogador, inimigos):
    vivos = inimigos_vivos(inimigos)
    if not vivos:
        print("Não existem inimigos vivos.")
        return

    listar_inimigos(inimigos)

    # Validação: só aceita números dentro do intervalo apresentado
    try:
        escolha = int(input("Escolha o número do inimigo: "))
    except ValueError:
        print("Erro: tem de introduzir um número.")
        return

    if escolha < 1 or escolha > len(vivos):
        print(f"Erro: escolha um número entre 1 e {len(vivos)}.")
        return

    inimigo = vivos[escolha - 1]

    # Ataque do jogador (10 a 20), a vida do inimigo nunca fica abaixo de zero
    dano = random.randint(10, 20)
    inimigo["vida"] = max(0, inimigo["vida"] - dano)
    print(f"\nAtacaste o {inimigo['nome']} e causaste {dano} de dano.")

    if inimigo["vida"] == 0:
        jogador["pontos"] += inimigo["pontos"]
        print(f"O {inimigo['nome']} foi derrotado! Ganhaste {inimigo['pontos']} pontos.")
    else:
        print(f"O {inimigo['nome']} ficou com {inimigo['vida']} de vida.")
        # Contra-ataque (entre 5 e o ataque do inimigo)
        dano_inimigo = random.randint(5, inimigo["ataque"])
        jogador["vida"] = max(0, jogador["vida"] - dano_inimigo)
        print(f"O {inimigo['nome']} contra-atacou e causou {dano_inimigo} de dano.")
        print(f"Ficaste com {jogador['vida']} de vida.")


def consultar_estado(jogador, inimigos):
    vivos = len(inimigos_vivos(inimigos))
    derrotados = len(inimigos) - vivos
    print("\n===== ESTADO DO JOGADOR =====")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuação: {jogador['pontos']}")
    print(f"Inimigos derrotados: {derrotados}")
    print(f"Inimigos vivos: {vivos}")
    print(f"Poções disponíveis: {jogador['pocoes']}")


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Não tens poções disponíveis.")
    elif jogador["vida"] >= VIDA_MAXIMA_POCAO:
        print(f"Já tens {VIDA_MAXIMA_POCAO} ou mais pontos de vida, não podes usar poção.")
    else:
        # Recupera 25 pontos sem ultrapassar os 300
        jogador["vida"] = min(VIDA_MAXIMA_POCAO, jogador["vida"] + CURA_POCAO)
        jogador["pocoes"] -= 1
        print(f"Usaste uma poção! Vida atual: {jogador['vida']} | Poções restantes: {jogador['pocoes']}")


def jogar():
    titulo()
    jogador = criar_jogador()
    inimigos = criar_inimigos()

    while True:
        opcao = menu()

        if opcao == 1:
            if not inimigos_vivos(inimigos):
                print("Todos os inimigos foram derrotados!")
                break
            atacar_inimigo(jogador, inimigos)
        elif opcao == 2:
            consultar_estado(jogador, inimigos)
        elif opcao == 3:
            listar_inimigos(inimigos)
        elif opcao == 4:
            usar_pocao(jogador)
        elif opcao == 5:
            print("Fugiste da batalha.")
            break
        else:
            print("Opção inválida.")

        if jogador["vida"] <= 0:
            print("Ficaste sem vida. Fim de jogo!")
            break

        if not inimigos_vivos(inimigos):
            print(f"Parabéns! Derrotaste todos os inimigos e conquistaste {jogador['pontos']} pontos.")
            break


if __name__ == "__main__":
    jogar()

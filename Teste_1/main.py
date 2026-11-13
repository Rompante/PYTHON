import random
from foncoes import menu,inimigos_vivos,atacar_inimigo,consultar_estado,listar_inimigos,usar_pocao,criar_jogador,criar_inimigos

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
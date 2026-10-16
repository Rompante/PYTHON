from random import randint
import os
resposta = "S"
while resposta == "S":
    os.system("clear")
    # Declarar e inicializar as variáveis
    tentativas = 0
    numGerado = randint(1, 100)
    print(numGerado)
    #Ciclo para as tentativas
    while tentativas < 7:

        tentativas = tentativas +1

        meuNumero = int(input("Tente o valor gerado: "))

        while meuNumero < 1 or meuNumero > 100:
                print("Valor inválido! O valor deve estar entre 1 e 100.")
                meuNumero = int(input("Tente Novamente: "))
                os.system("clear")

        if meuNumero == numGerado:
            print(f"Parabéns! Acertou em {tentativas} tentativas")
            break
        tentativas = tentativas +1
        if meuNumero > numGerado:
            print("O número gerado é menor que o da tentativa.")
        else:
            print("O número gerado é maior que o da tentativa")

        if tentativas >= 7:
             print(f"Que pena! O numeor foi {numGerado}")

        resposta = input ("Deseja jogar Novamente? (S/N)").upper()
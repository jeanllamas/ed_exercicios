def exercicio1():
    vetor = []
    for i in range(5):
        vetor.append(int(input("Digite um número inteiro: ")))
    print(vetor)


def exercicio2():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    if num1 < num2:
        print(f"\nOs números entre {num1} e {num2} são", end=" ")
        for i in range(num1 + 1, num2):
            print(i, end=" ")
    elif num1 > num2:
        print(f"\nOs números entre {num2} e {num1} são", end=" ")
        for i in range(num1 - 1, num2, -1):
            print(i, end=" ")


def exercicio3():
    vetor = []
    soma = 0
    mult = 1

    for i in range(5):
        vetor.append(int(input(f"Digite o {i+1}º nº inteiro: ")))
        soma += vetor[i]
        mult *= vetor[i]

    print("\nNúmeros inseridos: ", end="")
    for i in range(5):
        print(vetor[i], end=" ")

    print(f"\nSomatório: {soma}\nMultiplicação: {mult}")


def exercicio4():
    vetor = []

    for i in range(5):
        vetor.append(float(input(f"Digite o {i+1}º número: ")))
        vetor.sort()
        vetor.reverse()

    print(f"\nO maior número da lista é {vetor[0]}")


def exercicio5():
    vetor = [""] * 10
    consoantes = []

    for i in range(10):
        while True:
            caractere = input(f"Insira o {i + 1}º caractere: ")

            if len(caractere) == 1:
                vetor[i] = caractere
                if caractere.upper() not in ("A", "E", "I", "O", "U"):
                    consoantes.append(vetor[i])
                break
            else:
                print("\nInsira apenas um caractere.\n")

    print(f"\nAo todo, foram lidas {len(consoantes)} consoantes:")
    print(consoantes)


def exercicio6():
    pass


def exercicio7():
    pass


def exercicio8():
    pass


def exercicio9():
    pass


def exercicio10():
    pass


def exercicio11():
    pass


def exercicio12():
    pass


def exercicio13():
    pass


def exercicio14():
    pass


def exercicio15():
    pass


def exercicio16():
    pass


opcoes = {}  # Dicionário de opções

for i in range(1, 17):  # Criando chave de opções de 1 a 16
    opcoes[i] = globals()[f"exercicio{i}"]

while True:  # Acesso aos exercícios
    escolha = int(input("Insira o número do exercício (1 a 16): "))
    print()

    if escolha in opcoes:
        opcoes[escolha]()
        fim = input("\nExercício encerrado. Deseja voltar ou sair? (V/S) ")
        if fim.upper() != "V":
            break
    else:
        print("Opção inválida. Tente novamente.\n")

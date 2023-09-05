def exercicio1():
    """Perguntar o preço de três produtos e informar qual deve comprar,
    sabendo que a decisão é sempre o mais barato"""
    p1 = float(input("Preço do primeiro produto: "))
    p2 = float(input("Preço do segundo produto: "))
    p3 = float(input("Preço do terceiro produto: "))

    if p1 < p2 and p1 < p3:
        produto_barato = "primeiro"
        preco = p1
    elif p2 < p1 and p2 < p3:
        produto_barato = "segundo"
        preco = p2
    elif p3 < p1 and p3 < p2:
        produto_barato = "terceiro"
        preco = p3

    print(f"O {produto_barato} produto é o mais barato, custando R${preco}")


def exercicio2():
    pass


def exercicio3():
    pass


def exercicio4():
    pass


def exercicio5():
    pass


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


opcoes = {}  # Dicionário de opções

for i in range(1, 11):  # Criando chave de opções de 1 a 10
    opcoes[i] = globals()[f"exercicio{i}"]

while True:  # Acesso aos exercícios
    escolha = int(input("Insira o número do exercício (1 a 10): "))

    if escolha in opcoes:
        opcoes[escolha]()
        fim = input("\nExercício encerrado. Deseja voltar ou sair? (V/S) ")
        if fim.upper() != "V":
            break
           break

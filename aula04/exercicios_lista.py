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
    temp_mes = []
    nome_mes = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]
    media = 0
    temps_acima = []

    print("Insira as temperaturas em °C de Janeiro a Dezembro:")
    for i in range(12):
        temp_mes.append(float(input(f"{i+1} - {nome_mes[i]}: ")))
        media += temp_mes[i]
    media /= 12

    for i in range(12):
        if temp_mes[i] > media:
            temps_acima.append(f"{i+1} - {nome_mes[i]}: {temp_mes[i]:.2f}°C")

    print(f"\nA média anual de temperatura é {media:.2f}°C")
    print(f"Os meses com temperatura acima da média são:")
    for i in temps_acima:
        print(i)


def exercicio7():
    print("Números ímpares entre 1 e 50")
    for num_impar in range(1, 50, 2):
        print(num_impar, end=" ")


def exercicio8():
    print("Tabuada de 1 a 10")
    numero = int(input("Insira um número: "))

    for i in range(1, 11):
        print(f"{numero} X {i} = {numero*i}")


def exercicio9():
    par, impar = 0, 0

    for i in range(10):
        numero = int(input(f"Insira o {i+1}º número: "))
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1
    print(f"\nForam inseridos {par} números pares e {impar} números ímpares")


def exercicio10():
    num = int(input("Calcular fatorial de: "))
    fatorial = 1

    for i in range(num, 0, -1):
        fatorial *= i

    print(f"{num}! = {fatorial}")


def exercicio11():
    codigo, altura, massa = [], [], []
    media_altura, media_massa = 0, 0

    while True:
        codigo.append(int(input("Código: ")))
        if 0 in codigo:
            codigo.pop()
            break
        altura.append(float(input("Altura: ")))
        massa.append(float(input("Massa muscular: ")))
        print()

    for i in range(len(codigo)):
        media_altura += altura[i]
        media_massa += massa[i]
    media_altura /= len(codigo)
    media_massa /= len(codigo)

    cli_mais_alto = altura.index(max(altura))
    cli_mais_massa = massa.index(max(massa))
    cli_mais_baixo = altura.index(min(altura))
    cli_menos_massa = massa.index(min(massa))

    print(
        f"""\nA média de altura dos clientes é de {media_altura:.2f}m
A média de massa muscular dos clientes é de {media_massa:.2f}kg\n
O cliente mais alto é o {codigo[cli_mais_alto]} com {altura[cli_mais_alto]:.2f}m e {massa[cli_mais_alto]:.2f}kg
O cliente mais baixo é o {codigo[cli_mais_baixo]} com {altura[cli_mais_baixo]:.2f}m e {massa[cli_mais_baixo]:.2f}kg\n
O cliente com mais massa é o {codigo[cli_mais_massa]} com {massa[cli_mais_massa]:.2f}kg e {altura[cli_mais_massa]:.2f}m
O cliente com menos massa é o {codigo[cli_menos_massa]} com {massa[cli_menos_massa]:.2f}kg e {altura[cli_menos_massa]:.2f}m"""
    )


def exercicio12():
    cidade = []
    veiculos = []
    acidentes = []
    media_veiculos = 0
    media_acidentes = 0
    qtd_2k = 0

    for i in range(5):
        cidade.append(int(input(f"Código da {i+1}ª cidade: ")))
        veiculos.append(int(input("Nº de veiculos: ")))
        acidentes.append(int(input("Nº de acidentes: ")))
        print()

        media_veiculos += veiculos[i]
        if veiculos[i] < 2000:
            media_acidentes += acidentes[i]
            qtd_2k += 1

    media_veiculos /= 5
    media_acidentes /= qtd_2k

    print(
        f"""Maior indíce de acidentes: {max(acidentes)} em {cidade[acidentes.index(max(acidentes))]}
Menor índice de acidentes: {min(acidentes)} em {cidade[acidentes.index(min(acidentes))]}\n
Média de veiculos nas cinco cidades: {media_veiculos:.2f}\n
Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes:.2f}"""
    )


def exercicio13():
    while True:
        atleta = input("Atleta: ")
        if atleta == "":
            break

        saltos = []
        media = 0
        for i in range(5):
            saltos.append(float(input(f"{i+1}º Salto: ")))
            media += saltos[i]

        melhor = max(saltos)
        pior = min(saltos)
        media -= melhor + pior
        media /= 3

        print(
            f"""\nMelhor salto: {melhor:.1f} m
Pior salto: {pior:.1f} m
Média dos demais saltos: {media:.1f} m\n
Resultado final:\n{atleta}: {media:.1f} m\n\n"""
        )


def exercicio14():
    atleta = input("Atleta: ")
    notas = []
    media = 0

    for i in range(7):
        notas.append(float(input(f"{i+1}ª Nota: ")))
        media += notas[i]

    melhor = max(notas)
    pior = min(notas)

    media -= melhor + pior
    media /= 5

    print(
        f"""\nResultado final
Atleta: {atleta}
Melhor nota: {melhor:.1f}
Pior nota: {pior:.1f}
Média: {media:.2f}"""
    )


def exercicio15():
    produto, qtd, preco = [], [], []
    preco_total_lista = 0

    while True:
        produto.append(input("Produto: "))
        if "fim" in produto:
            produto.pop()
            break
        qtd.append(int(input("Quantidade: ")))
        preco.append(float(input("Preço: ")))

        preco_total = qtd[-1] * preco[-1]
        print(f"Valor da compra: R${preco_total:.2f}\n")

        preco_total_lista += preco_total
    print(f"\nValor total da lista de compras: R${preco_total_lista:.2f}")


def exercicio16():
    lista, pares, impares = [], [], []

    while True:
        num = int(input("Insira um número: "))
        if not 0 < num <= 11:
            break

        lista.append(num)

        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print("\nLista original: ", end="")
    for i in lista:
        print(f"{i} ", end="")

    print("\nPares: ", end="")
    for i in pares:
        print(f"{i} ", end="")

    print("\nÍmpares: ", end="")
    for i in impares:
        print(f"{i} ", end="")


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

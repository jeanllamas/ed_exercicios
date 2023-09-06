def exercicio1():
    numero, nums25, nums50, nums75, nums100 = 0, 0, 0, 0, 0

    while numero >= 0:
        numero = int(input("Digite um número: "))

        if 0 <= numero <= 25:
            nums25 += 1
        elif 26 <= numero <= 50:
            nums50 += 1
        elif 51 <= numero <= 75:
            nums75 += 1
        elif 76 <= numero <= 100:
            nums100 += 1
        elif numero > 100:
            continue
        else:
            break

    print(f"\nContagem de números inseridos:")
    print(f"0 a 25: {nums25} números")
    print(f"26 a 50: {nums50} números")
    print(f"51 a 75: {nums75} números")
    print(f"76 a 100: {nums100} números\n")


def exercicio2():
    qtd = 0
    soma = 0

    while True:
        numero = float(input(f"Informe a {qtd+1}ª nota: "))

        if numero < 0:
            break
        else:
            qtd += 1
            soma += numero

    media = soma / qtd

    print(f"\nA média aritmética das notas é {media}\n")


def exercicio3():
    qtd = 0
    soma = 0
    turma = ""

    while True:
        idade = int(input(f"Informe a {qtd+1}ª idade: "))

        if idade < 0:
            break
        else:
            qtd += 1
            soma += idade

    media = soma / qtd

    if 0 <= media <= 25:
        turma = "jovem"
    elif 26 <= media <= 60:
        turma = "adulta"
    elif media > 60:
        turma = "idosa"

    print(f"\nA média de {media} anos de idade indica que a turma é {turma}\n")


def exercicio4():
    votosA, votosB, votosC = 0, 0, 0
    while True:
        voto = input("Insira seu voto no candidato A, B ou C: ").upper()

        if voto == "A":
            votosA += 1
        elif voto == "B":
            votosB += 1
        elif voto == "C":
            votosC += 1
        else:
            print("Candidato inválido")
            break

    print(
        f"\nVotos recebidos pelos candidatos dentre {votosA+votosB+votosC} eleitores:"
        f"\nA - {votosA} votos"
        f"\nB - {votosB} votos"
        f"\nC - {votosC} votos"
    )


def exercicio5():
    while True:
        n1 = float(input("\nPrimeira nota: "))
        if n1 == 9:
            break
        n2 = float(input("Segunda nota: "))
        if n2 == 9:
            break
        n3 = float(input("Terceira nota: "))
        if n3 == 9:
            break

        media = (n1 + n2 + n3) / 3

        print("Nota final:", end=" ")
        if media >= 7:
            print(f"{media}  Aprovado")
        if media < 7:
            print(f"{media}  Reprovado")
        if media == 10:
            print(f"{media}  Aprovado com Distinção")


def exercicio6():
    while True:
        cidade = input("\nNome de uma cidade: ")
        if cidade.lower() == "fim":
            break

        grausC = float(input("Temperatura em graus Celsius (°C): "))

        grausF = (9 * grausC + 160) / 5

        print(f"\n{grausC}°C da cidade de {cidade} equivalem a {grausF}°F")


def exercicio7():
    while True:
        regiao = input("\nRegião das vendas: ")

        if regiao.lower() != "fim":
            print("\nInsira o valor das vendas, em R$, de")
            jan = float(input("Janeiro: "))
            fev = float(input("Fevereiro: "))
            mar = float(input("Março: "))
            abr = float(input("Abril: "))

            media_vendas = (jan * 1 + fev * 4 + mar * 1 + abr * 4) / (1 + 4 + 1 + 4)

            print(f"\nEm janeiro, {regiao} obteve R${jan:.2f};")
            print(f"Em fevereiro, {regiao} obteve R${fev:.2f};")
            print(f"Em março, {regiao} obteve R${mar:.2f};")
            print(f"E em abril, {regiao} obteve R${abr:.2f}.")

            print(
                f"\nTotalizando em {regiao} uma média ponderada de R${media_vendas:.2f} em vendas."
            )
        else:
            break


opcoes = {}  # Dicionário de opções

for i in range(1, 8):  # Criando chave de opções de 1 a 7
    opcoes[i] = globals()[f"exercicio{i}"]

while True:  # Acesso aos exercícios
    escolha = int(input("Insira o número do exercício (1 a 7): "))

    if escolha in opcoes:
        opcoes[escolha]()
        fim = input("\nExercício encerrado. Deseja voltar ou sair? (V/S) ")
        if fim.upper() != "V":
            break

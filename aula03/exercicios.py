def exercicio1():
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
    turno = input("Em que turno você estuda?\nM - matutino\n V - vespertino\n N - noturno\n")
    if turno == "M":
        print("Bom dia!")
    elif turno == "V":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Valor inválido")

def exercicio3():
    numero = float(input("Insira um número: "))

    if numero >= 0:
        raiz_qdd = numero ** 0.5
    else:
        print("Número inválido")

def exercicio4():
    salario_atual = float(input("Insira o seu salário: "))

    salario_minimo = 1320

    if salario_atual <= salario_minimo:
        aumento = salario_atual * 0.2
        salario_ajustado = salario_atual + aumento
        percentual = "20%"

    elif salario_atual > salario_minimo and salario_atual <= salario_minimo * 2:
        aumento = salario_atual * 0.15
        salario_ajustado = salario_atual + aumento
        percentual = "15%"

    elif salario_atual > salario_minimo * 2 and salario_atual <= salario_minimo * 5:
        aumento = salario_atual * 0.1
        salario_ajustado = salario_atual + aumento
        percentual = "10%"

    elif salario_atual > salario_minimo * 5:
        aumento = salario_atual * 0.05
        salario_ajustado = salario_atual + aumento
        percentual = "5%"

    print(f"\nSalário antes do reajuste: R${salario_atual}")
    print(f"Percentual de aumento: {percentual}")
    print(f"Valor do aumento: R${aumento}")
    print(f"Novo salário: R${salario_ajustado}")

def exercicio5():
    numero = int(input("Insira um número inteiro: "))

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

def exercicio6():
    macas = int(input("Quantas maçãs foram compradas? "))

    if macas < 12:
        preco = 0.3
    elif macas > 12:
        preco = 0.25

    valor_total = macas * preco

    print(f"Você comprou {macas} maçãs, portanto o valor da compra é R${valor_total}")

def exercicio7():
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    n3 = float(input("Terceira nota: "))

    media = (n1+n2+n3)/3

    if media >= 7:
        print(f"Nota: {media}  Aprovado")
    if media < 7:
        print(f"Nota: {media}  Reprovado")
    if media == 10:
        print(f"Nota: {media}  Aprovado com Distinção")

def exercicio8():
    print('Insira em R$ o valor das vendas do mês de')
    jan = float(input('Janeiro: '))   
    fev = float(input('Fevereiro: '))
    mar = float(input('Março: '))
    abr = float(input('Abril: '))

    ponderada = (jan*1 + fev*4 + mar*1 + abr*4)/(1+4+1+4)

    print(f'Janeiro - R${jan}')
    print(f'Fevereiro - R${fev}')
    print(f'Março - R${mar}')
    print(f'Abril - R${abr}')

    print(f'\nMédia ponderada de vendas: R${ponderada}')

    if jan > ponderada:
        print("\nVendas do mês de Janeiro superiores à média do período")
    if fev > ponderada:
        print("\nVendas do mês de Fevereiro superiores à média do período")
    if mar > ponderada:
        print("\nVendas do mês de Março superiores à média do período")
    if abr > ponderada:
        print("\nVendas do mês de Abril superiores à média do período")

def exercicio9():
    letra = input("Insira uma letra: ").upper()

    if letra == "F":
        print("F - Feminino")
    elif letra == "M":
        print("M - Masculino")
    else:
        print("Sexo inválido")

def exercicio10():
    letra = input("Insira uma letra: ").upper()

    if letra == ("A" or "E" or "I" or "O" or "U"):
        print(f"{letra} é uma vogal")
    else:
        print(f"{letra} é uma consoante")


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
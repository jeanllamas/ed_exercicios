def exercicio1():
    ultimo = 10
    operacao = ""
    fila = list(range(1, ultimo + 1))

    while operacao != "S":
        print(f"\nExistem {len(fila)} clientes na fila")
        print(f"fila atual: {fila}")
        print("Digite F para adicionar um cliente ao fim da fila,")
        print("ou A para realizar o atendimento. S para sair.")

        operacao = input("operação (F, A, ou S): ")

        if operacao == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            ultimo += 1
            fila.append(ultimo)
        else:
            print("Operação inválida! Digite apenas F, A ou S!")


def exercicio2():
    pacientes = []
    nome = ""

    while nome.lower() != "fim":
        print(f"\nExistem {len(pacientes)} pacientes na fila")
        print(f"fila atual: {pacientes}")
        print("Digite F para adicionar um paciente ao fim da fila")
        print(
            'ou A para realizar o atendimento. Digite "fim" no nome do paciente para sair.'
        )

        operacao = input("operação (F, A, ou S): ").upper()

        if operacao == "A":
            if len(pacientes) > 0:
                atendido = pacientes.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operacao == "F":
            nome = input("Nome do paciente: ")
            pacientes.append(nome)
        else:
            print("Operação inválida! Digite apenas F, A ou S!")


opcoes = {}  # Dicionário de opções

for i in range(1, 3):  # Criando chave de opções
    opcoes[i] = globals()[f"exercicio{i}"]

while True:  # Acesso aos exercícios
    escolha = int(input("Insira o número do exercício (1 a 2): "))
    print()

    if escolha in opcoes:
        opcoes[escolha]()
        fim = input("\nExercício encerrado. Deseja voltar ou sair? (V/S) ")
        if fim.upper() != "V":
            break
    else:
        print("Opção inválida. Tente novamente.\n")

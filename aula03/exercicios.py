def exercicio1():
   '''Perguntar o preço de três produtos e informar qual deve comprar,
   sabendo que a decisão é sempre o mais barato'''
    p1 = float(input('Preço do primeiro produto: '))
    p2 = float(input('Preço do segundo produto: '))
    p3 = float(input('Preço do terceiro produto: '))

    if (p1 < p2 && p1 < p3):
        produto_barato = "primeiro"
        preco = p1
    elif (p2<p1 && p2<p3):
        produto_barato = "segundo"
        preco = p2
    elif (p3<p1 && p3<p2):
        produto_barato = "terceiro"
        preco = p3

    print(f"O {produto_barato} produto é o mais barato, custando R${preco}")

def exercicio2():

def exercicio3():

def exercicio4():

def exercicio5():

def exercicio6():

def exercicio7():

def exercicio8():
    
def exercicio9():
    
def exercicio10():

opcoes = {} #Dicionário de opções

for i in range(1, 9): #Criando chave de opções de 1 a 8
    opcoes[i] = globals()[f'exercicio{i}']

while True: #Acesso aos exercícios
    escolha = int(input('Insira o número do exercício (1 a 8): '))

    if escolha in opcoes:
        opcoes[escolha]()
        fim = input('\nExercício encerrado. Deseja voltar ou sair? (V/S) ')
        if fim.upper() != 'V':
            break

def exercicio1():
    # Receba dois números e exiba o resultado da sua soma
    num1 = int(input("\033[1;35;40mDigite um número:\033[m "))  # Entrada do primeiro número
    num2 = int(input("\033[1;31;42mDigite mais um número:\033[m "))  # Entrada do segundo número
    print(f"\n\033[1;33;44mA soma de \033[7m{num1}+{num2} é {num1+num2}\033[m")  # Saída da soma dos números

def exercicio2():
    '''Receba dois números e ao final mostre a soma, subtração,
    multiplicação e a divisão dos números lidos.'''

    num1 = int(input("\033[4;30;42mDigite um número:\033[m "))      # Entrada do primeiro número
    num2 = int(input("\033[4;32;45mDigite mais um número:\033[m ")) # Entrada do segundo número

    print(f"\n\033[1;31;40m(+)Soma: {num1+num2}")          # Saída do cálculo da soma
    print(f"\n\033[1;32;41m(-)Subtração: {num1-num2}")     # Saída do cálculo da subtração
    print(f"\n\033[1;33;42m(*)Multiplicação: {num1*num2}") # Saída do cálculo da multiplicação
    print(f"\n\033[1;35;43m(/)Divisão: {num1/num2}\033[m") # Saída do cálculo da divisão

def exercicio3():
    '''Determinar o consumo médio de um automóvel sendo fornecida a distância
    total percorrida pelo automóvel e o total de combustível gasto'''

    #Entrada da distância percorrida
    distancia = float(input("\033[1;34;46mDigite a distância percorrida em km:\033[m "))

    #Entrada do combustível gasto
    combustivel = float(input("\033[1;35;41mDigite o consumo de combustível em litros:\033[m "))

    #Saída do consumo médio
    print(f"\n\033[1;33;42mO consumo médio do automóvel é de {distancia / combustivel}km/l\033[m")

def exercicio4():
    '''Leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas
    por ele no mês (em dinheiro). Sabendo que este vendedor ganha 7,5% de comissão
    sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário líquido
    no final do mês'''

    nome = input('\033[1;35;42mQual é o seu nome?\033[m ') #Entrada do nome
    salario = float(input('\033[1;32;45mInsira seu salário fixo:\033[m ')) #Entrada do salário fixo
    vendas = float(input('\033[1;30;46mInsira em R$ o ganho por suas vendas:\033[m ')) #Entrada do total de vendas em R$

    #Saída do nome, salário fixo e o novo salário líquido
    print(f'\033[1;31;43m{nome}, sabendo que seu salário fixo é R${salario},\
    o seu salário líquido deste mês será \033[7mR${salario+vendas*0.075}\033[m')

def exercicio5():
    '''Leia o nome de um aluno e as notas das cinco provas que ele obteve no semestre.
    No final informar o nome do aluno e a sua média (aritmética) indicando se foi aprovado ou reprovado'''

    nome = input('\033[1;31;44mQual é o seu nome?\033[m ') #Entrada do nome do aluno

    nota = 0 #Inicialização da variável

    #Entrada das cinco notas obtidas no semestre
    for i in range(1, 6):
        nota += float(input(f'\033[1;32;45mNota da prova {i}:\033[m '))

    media = nota / 5 #Cálculo da média de notas

    #Verificação da nota para caso de aprovação
    if (media >= 6):
        situacao = "aprovado"
    else:
        situacao = "reprovado"

    #Saída do nome do aluno, sua média de notas e a situação
    print(f'\n\033[1;36;47m{nome}, sua média de notas é {media}, portanto foi {situacao}.\033[m')

def exercicio6():
    '''Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores
    de forma que a variável A passe a possuir o valor da variável B e a variável B
    passe a possuir o valor da variável A. Apresentar os valores trocados'''

    #Entrada de valores de A e B
    A = float(input('\033[7;31;43mDigite um valor numérico para A:\033[m '))
    B = float(input('\033[7;36;47mDigite um valor numérico para B:\033[m '))

    #Trocando A por B e vice-versa com auxílio de uma terceira variável
    C = A
    A = B
    B = C

    #Saída das variáveis A e B trocadas
    print(f'\n\033[1;33;42mAgora A vale {A} e B vale {B}\033[m')

def exercicio7():
    '''Receba uma temperatura em graus Celsius e apresente como resultado a conversão
    em graus Fahrenheit. A fórmula de conversão é: F=(9*C+160) / 5, sendo F a temperatura
    em Fahrenheit e C a temperatura em Celsius.'''

    #Entrada da temperatura em Celsius
    C = float(input('\033[1;31;45mInsira uma temperatura em graus Celsius:\033[m '))

    #Conversão de Celsius para Fahrenheit
    F = (9*C+160)/5

    #Saída da temperatura convertida
    print(f'\n\033[4;32;44m{C}°C equivalem a {F}°F\033[m')

def exercicio8():
    ''' Receba os valores das vendas dos meses de janeiro, fevereiro, março e abril
    e calcule a média ponderada das vendas dos quatro meses, considerando que janeiro
    e março tem peso 1, fevereiro e abril tem peso 4 cada. No final mostrar as vendas
    dos quatro meses e a média ponderada calculada '''

    # Entrada de vendas de Janeiro a Abril
    print('\033[1;31;40mInsira em R$ o valor das vendas do mês de')
    jan = float(input('\033[1;32;44mJaneiro:\033[m '))   
    fev = float(input('\033[1;36;45mFevereiro:\033[m '))
    mar = float(input('\033[1;35;46mMarço:\033[m '))
    abr = float(input('\033[1;34;42mAbril:\033[m '))

    # Cálculo da média ponderada com cada peso
    ponderada = (jan*1 + fev*4 + mar*1 + abr*4)/(1+4+1+4)

    # Saída dos valores de cada mês
    print(f'\n\033[1;32;44mJaneiro - R${jan}\033[m\
        \n\033[1;36;45mFevereiro - R${fev}\033[m\
        \n\033[1;35;46mMarço - R${mar}\033[m\
        \n\033[1;34;42mAbril - R${abr}\033[m')

    # Saída da média ponderada
    print(f'\n\033[1;37;40mMédia ponderada de vendas: R${ponderada}\033[m')

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
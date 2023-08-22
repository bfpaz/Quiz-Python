import time
lista = []

def ler_perguntas():  #FUNÇÃO PARA LER O ARQUIVO E ARMAZENAR AS PERGUNTAS DENTRO DE UMA LISTA
    with open('perguntas.txt ', 'r') as arq:
        arquivo = arq.read()
        arquivo = arquivo.split('\n')
        for x in arquivo:
            if len(x) > 0: # TRATAMENTO DA ULTIMA QUEBRA DE PÁGINA
                lista.append(x.split(","))

def iniciar_jogo(): #FUNÇÃO QUE INICIA O JOGO
    import random
    aleatorio = random.sample(lista, 10) #SELECIONANDO 10 ITENS ALEATÓRIOS DA LISTA
    respostas_certas = 0
    for x in range(0, len(aleatorio)): #LOOP QUE EXIBIRÁ AS PERGUNTAS
        perguntas = {
            f'Q{x+1}.': {
                'pergunta': aleatorio[x][0],
                'respostas': {
                    'a': aleatorio[x][1],
                    'b': aleatorio[x][2],
                    'c': aleatorio[x][3],
                    'd': aleatorio[x][4],
                    'e': aleatorio[x][5]},
                'resposta_certa': aleatorio[x][6]
            },
        }
        for pk, pv in perguntas.items():
            print(f'{pk}: {pv["pergunta"]}')
            for rk, rv in pv['respostas'].items():
                print(f'{rk}) {rv}')
            print()
            resp_user = input("Sua resposta: ")
            if resp_user.lower() == pv['resposta_certa']:
                print("\nRESPOSTA CERTA!")
                respostas_certas += 1
                time.sleep(2)
            else:
                print("\nVOCÊ ERROU!")
                time.sleep(2)
            print()
    #ESTA ETAPA ABAIXO REALIZARÁ O CÁLCULO DA PONTUAÇÃO DO JOGADOR E ARQUIVARÁ NO ARQUIVO RANKING
    aproveitamento = respostas_certas / len(aleatorio) * 100
    print(f"{nome.upper()} VOCÊ ACERTOU {respostas_certas} PERGUNTAS E TEVE {aproveitamento}% DE APROVEIRAMENTO.")
    time.sleep(2)
    with open('ranking.txt', 'a') as arq:
        arq.write(f'{nome.upper()}, {aproveitamento:.2f}\n')

def ranking(): #FUNÇÃO QUE LÊ O ARQUIVO RANKING E EXIBE EM TELA
    with open('ranking.txt ', 'r') as rkg:
        arquivo = rkg.read()
        arquivo = arquivo.split('\n')
        l = []
        for x in arquivo: # LOOP PARA EXIBIR O RANKING
            if len(x) > 0:
                l.append(x.split(','))
                print(f'\033[1:34:40m{x}\033[m') #PRINTA COM FONTE EM AZUL COM FUNDO PRETO
    time.sleep(3)

def excluir_pergunta(): # FUNÇÃO PARA EXCLUIR PERGUNTA DO ARQUIVO
    cont = 1
    for x in lista: #LOOP QUE EXIBE TODAS AS PERGUNTAS
        print(f'Pergunta {cont}: {x}')
        cont += 1
    excl = int(input('Qual pergunta deseja excluir: '))
    lista.pop(excl-1) #EXCLUI A PERGUNTA DA LISTA
    atualizar_perguntas() #INVOCAÇÃO DA FUNÇÃO PARA ATUALIZAR O ARQUIVO CONFORME A LISTA

def atualizar_perguntas(): # FUNÇÃO QUE ATUALIZA O ARQUIVO
    arq = open('perguntas.txt', "w")
    for i in lista: # LOOP QUE REESCREVE O ARQUIVO CONFORME A LISTA ATUALIZADA
        arq.write(f'{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]},{i[6]}\n')
    arq.close()

def adicionar_perguntas(): # FUNÇÃO PARA ADICIONAR PERGUNTAS AO ARQUIVO
    p = input('Pergunta: ')
    a = input('Alternativa a): ')
    b = input('Alternativa b): ')
    c = input('Alternativa c): ')
    d = input('Alternativa d): ')
    e = input('Alternativa e): ')
    correta = input('Alternativa correta: ')
    arq = open('perguntas.txt', 'a') # ETAPA ONDE SE ATUALIZA O ARQUIVVO EXISTENTE, ACRESCENTANDO APENAS A NOVA PERGUNTA
    arq.write(f'{p},{a},{b},{c},{d},{e},{correta}\n')
    arq.close()

def alterar_pergunta(): # FUNÇÃO PARA ALTERAR PERGUNTA
    cont = 1
    for x in lista: # LOOP QUE EXIBE AS PERGUNTAS EXISTENTES
        print(f'Pergunta {cont}: {x}')
        cont += 1
    alt = int(input('Qual pergunta deseja alterar: '))
    novo = []
    p = input('Pergunta: ')
    novo.append(p)
    a = input('Alternativa a): ')
    novo.append(a)
    b = input('Alternativa b): ')
    novo.append(b)
    c = input('Alternativa c): ')
    novo.append(c)
    d = input('Alternativa d): ')
    novo.append(d)
    e = input('Alternativa e): ')
    novo.append(e)
    correta = input('Alternativa correta: ')
    novo.append(correta)
    lista[alt-1] = novo # TROCA A PERGUNTA
    atualizar_perguntas() # INVOCAÇÃO DA FUNÇÃO PARA ATUALIZAR O ARQUIVO CONFORME A LISTA

def menu_perguntas(): # MENU DE EDIÇÃO DAS PERGUNTAS
    ler_perguntas()  # INVOCAÇÃO DA FUNÇÃO DE DE LEITURA DO ARQUIVO DE PERGUNTAS
    while True:
        print('Digite uma das opções abaixo.')
        print('0 - para inserir perguntas.')
        print('1 - para alterar perguntas.')
        print('2 - para excluir perguntas.')
        print('3 - para voltar.')
        operação = input('Opção: ')
        if operação == '0':
            adicionar_perguntas()
        elif operação == '1':
            alterar_pergunta()
        elif operação == '2':
            excluir_pergunta()
        elif operação == '3':
            break
        else:
            print("Operação inválida!!!")

entrada = input('DESEJA ENTRAR NO MENU DE PERGUNTAS ANTES DE JOGAR?:\n' # PARTIDA DO JOGO
                'ENTRE COM [S] PARA SIM OU QUALQUER TECLA PARA SEGUIR.\n'
                '')

if entrada.upper() == 'S': # OPÇÃO CASO OPTAR POR EDITAR PERGUNTAS
    menu_perguntas()

while True: #MENU LOOP INFINITO
    ler_perguntas()  # INVOCAÇÃO DA FUNÇÃO DE DE LEITURA DO ARQUIVO DE PERGUNTAS
    print('\033[1:34:40mRANKING DE DESEMPENHO ATUAL\033[m\n')
    ranking()
    nome = input('\nDigite seu nome para jogar: ')
    iniciar_jogo()





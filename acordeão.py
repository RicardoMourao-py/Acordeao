# Começando o exercício progama
print('Design de Software')
print('Ricardo Mourão Rodrigues Filho')

# Explicação do Acordeão
print('Paciência Acordeão')
print('=================== \n')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. \n')
print('Existem apenas dois movimentos possíveis: \n')
print('1. Empilhar uma carta sobre a carta imediatamente anterior; ')
print('2. Empilhar uma carta sobre a terceira carta anterior. \n')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: \n')
print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. \n')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. \n')
input('Aperte [Enter] para iniciar o jogo... \n')

import random
# gerando uma função para criar o baralho:
def cria_baralho():
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"
    lista_espadas=['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠'] # Espadas
    lista_copas=['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']   # Copa
    lista_ouros=['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']   # Ouros
    lista_paus=['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']    # Paus
    lista_cartas = lista_espadas + lista_copas + lista_ouros + lista_paus
    lista_cartas_embaralhadas = random.sample(lista_cartas, 52)
    return lista_cartas_embaralhadas
#extraindo o naipe da carta
def extrai_naipe(carta):
    if len(carta)==2:
        return carta[1]
    elif len(carta)==3:
        return carta[2]
# extraindo o valor da carta 
def extrai_valor(carta):
    if len(carta)==2:
        return carta[0]
    elif len(carta)==3:
        return carta[0] + carta[1]
# definindo uma função para a movimentação das cartas 
def lista_movimentos_possiveis(baralho,posicao):
    if posicao==0:
        return []
    elif posicao==1:
        if extrai_valor(baralho[posicao])==extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao])==extrai_naipe(baralho[posicao-1]):
            return [1]
        else:
            return []
    elif posicao==2:
        if extrai_valor(baralho[posicao])==extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao])==extrai_naipe(baralho[posicao-1]):
            return [1]
        else:
            return []
    elif (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-3])) and (extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1])):
        return [1,3]
    elif extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-1]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-1]):
        return [1]
    elif extrai_valor(baralho[posicao]) == extrai_valor(baralho[posicao-3]) or extrai_naipe(baralho[posicao]) == extrai_naipe(baralho[posicao-3]):
        return [3]
    else: 
        return []
# criando a função de empilhar as cartas 
def empilha(baralho,posicao,destino):
    if lista_movimentos_possiveis(baralho, posicao)==[1,3] or lista_movimentos_possiveis(baralho, posicao)==[1] or lista_movimentos_possiveis(baralho, posicao)==[3]:
        baralho[destino-1]=baralho[posicao]
        del baralho[posicao]
        return baralho
    else:
        return baralho
# definindo uma função que verifica se há movimentos
def possui_movimentos_possiveis(lista):
    lista_verifica=[]
    i=0
    while i<len(lista):
        if lista_movimentos_possiveis(lista, i)==[1,3] or lista_movimentos_possiveis(lista, i)==[1] or lista_movimentos_possiveis(lista, i)==[3]:
            lista_verifica.append(i)
            i+=1
        else:
            i+=1
    if len(lista_verifica)!=0:
        return True
    else:
        return False
baralho=cria_baralho()
while True:
    print('O estado atual do baralho é: ')
    i=0
    while i<len(baralho):
        print(f'{i+1}. {baralho[i]}')
        i+=1
    posicao = int(input(f'Escolha uma carta de 1 a {i}: '))
    carta = baralho[posicao-1]
    print(f'A carta escolhida foi: {carta}')
    #print(extrai_naipe(carta))
    #print(extrai_valor(carta))
    posicao = posicao-1
    movimetacoes_possiveis = lista_movimentos_possiveis(baralho, posicao)
    if movimetacoes_possiveis == [1,3]:
        print(f'Os destinos possíveis para a carta escolhida é {posicao+1-3} ou {posicao+1-1}, que possui as cartas {baralho[posicao-3]} e {baralho[posicao-1]}, respectivamente.')
        uma_delas = int(input('A que posição deseja destinar a carta: '))
        destino = uma_delas
        print(f'O destino da sua carta será para a posição: {destino}')
        input('clique [enter] para confirmar')
    elif movimetacoes_possiveis== [1]:
        #destino=baralho[posicao-1]
        destino=posicao
        print(f'O destino possível da sua carta será para a posição {destino}, que possui a carta {baralho[posicao-1]}')
        input('clique [enter] para confirmar')
    elif movimetacoes_possiveis== [3]:
        #destino=baralho[posicao-3]
        destino=posicao-2
        print(f'O destino possível da sua carta será para a posição {destino}, que possui a carta {baralho[posicao-3]}')
        input('clique [enter] para confirmar')
    elif movimetacoes_possiveis== []:
        destino=[]
        print('Não há movimentos possíveis escolha outra posição')
        input('clique [enter] para confirmar')
    #print(lista_movimentos_possiveis(baralho, posicao))
    baralho = empilha(baralho, posicao, destino)
    print('====================================================')
    #i=0
    # while i<len(baralho):
    #     print(f'{i+1}. {baralho[i]}')
    #     i+=1
    verificando_novo_baralho=possui_movimentos_possiveis(baralho)
    if verificando_novo_baralho==False:
        print('O estado final do baralho é:' )
        i=0
        while i<len(baralho):
            print(f'{i+1}. {baralho[i]}')
            i+=1
        if len(baralho)==1:
            print('Parabéns você ganhou, conseguiu empilhar todas as cartas !!!!')
        else:
            print('Sem movimentações possíveis, não foi dessa vez, tente Novamente!' )
        break
    

    





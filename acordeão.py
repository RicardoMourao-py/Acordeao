# Começando o exercício progama
print('Design de Software')
print('Ricardo Mourão Rodrigues Filhos')

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
print('O estado atual do baralho é: ')

import random
# gerando uma função para criar o baralho:
def cria_baralho():
    lista_espadas=['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠'] # Espadas
    lista_copas=['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']   # Copa
    lista_ouros=['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']   # Ouros
    lista_paus=['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣']    # Paus
    lista_cartas = lista_espadas + lista_copas + lista_ouros + lista_paus
    lista_cartas_embaralhadas = random.sample(lista_cartas, 52)
    return lista_cartas_embaralhadas
i=0
while i<len(cria_baralho()):
    print(f'{i+1}. {cria_baralho()[i]}')
    i+=1

def extrai_naipe(carta):
    if len(carta)==2:
        return carta[1]
    elif len(carta)==3:
        return carta[2]
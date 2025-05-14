'''PROJETO001: Jogo de pedra, papel e tesoura.'''
#Autor: João Pedro Bento Severo
#Insta: @sadzin.dev*/

#Bibliotecas
from time import sleep
from random import randint

print('\n{ PROJETO 001 }\n')

#Opções de escolha para jogar
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

#Entrada para jogada
jogada = int(input('Qual é a sua jogada? '))

#Criação de lista para que haja o sorteio pela função 'randint' logo em seguida
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

#Condição de escape
if jogada not in [0, 1, 2]:
    print('OPÇÃO INVÁLIDA, tente novamente mais tarde.\n')
else:
    #Frase clássica junto com uma espera até o resultado do jogo
    print('\nJO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PO!!!\n')
    sleep(0.7)

    #Recapitulação das jogadas
    print('-=' * 14)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogada]}')
    print('-=' * 14)

    #Dicionário de resultados
    resultados = {
        (0, 2): 'JOGADOR VENCE',
        (2, 1): 'JOGADOR VENCE',
        (1, 0): 'JOGADOR VENCE',
        (2, 0): 'COMPUTADOR VENCE',
        (1, 2): 'COMPUTADOR VENCE',
        (0, 1): 'COMPUTADOR VENCE'
    }

    #Condições para determinar quem vence
    if jogada == computador:
        print('EMPATE\n')
    else:
        print(resultados.get((jogada, computador), 'ERRO DESCONHECIDO') + '\n')
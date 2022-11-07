# jogo de pedra,papel e tesoura

from random import randint
from time import sleep

print("#"*20)
print('BEM VINDO AO JOGO JOKENPO!')
print("#"*20)

print('\nAs regras do jogo são: \n\nPedra vence tesoura e perde para papel\nTesoura vence papel e perde para pedra\nPapel vence pedra e perde para tesoura\n\nSera escolhido então uma opção automatica para o computador e o jogador devera escolher entre as opções: \n\n0 - pedra\n1 - papel\n2 - tesoura\n')
jogador = int(input('Escolha a opção desejada: '))
lista = ['pedra','papel','tesoura']
computador = randint(0,2)

if jogador >= 0 and jogador <= 2:
   print('\nJO')
   sleep(0.6)
   print('KEN')
   sleep(0.6)
   print('PO!')
   sleep(0.6)
   print('\n\nA opção escolhida pelo jogador foi: {}'.format(lista[jogador]))
   print('A opção escolhida pelo computador foi: {}\n'.format(lista[computador]))
else:
    print('Opçao invalida!')

if jogador == 0 and computador == 1:
   print('O computador venceu!')
elif jogador == 0 and computador == 2:
   print('Você venceu!')
elif jogador == 0 and computador == 0:
   print('Deu empate!') 

if jogador == 1 and computador == 0:
   print('Você venceu!')
elif jogador == 1 and computador == 2:
   print('O computador venceu!')
elif jogador == 1 and computador == 1:
   print('Deu empate!')
   
if jogador == 2 and computador == 1:
   print('Você venceu!')
elif jogador == 2 and computador == 0:
   print('O computador venceu!')
elif jogador == 2 and computador == 2:
   print('Deu empate!')
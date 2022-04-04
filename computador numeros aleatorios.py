from random import randint
from time import sleep
computador = randint (0, 5)
print('-=-' * 20)
print('Irei pensar em um número, você consegue adivinhar?')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei?'))
print('CARREGANDO RESPOSTA...')
sleep (3)
if jogador == computador:
    print ('PARABÉNS! Você venceu')
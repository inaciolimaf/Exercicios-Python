from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 1 e 5. Tente adivinhar...')
Escol= randint(0,5)
print('-=-'*20)
Pens=int(input('Em que número você pensou?'))
print('PROCESSANDO...')
sleep(1)
if Escol==Pens:
    print('VOCÊ VENCEU!!!!')
else:
    print('Você perdeu!!! Eu pensei no {} e não no {}'.format(Escol, Pens))
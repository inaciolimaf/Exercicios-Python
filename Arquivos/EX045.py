from random import randint
from time import sleep
def venc():
    print('Você venceu')
def perdeu():
    print('O computador venceu')
print('Suas opções:\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA')
resp = int(input('QUAL É A SEU JOGADA?'))
print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO')
esc = randint(1, 3)
print('=-'*10)
if esc==1:
    print('O computador jogou PEDRA')
elif esc==2:
    print('O computador jogou PAPEL')
elif esc==3:
    print('O computador jogou TESOURA')
if resp==1:
    print('Você jogou PEDRA')
elif resp==2:
    print('Você jogou PAPEL')
elif resp==3:
    print('Você jogou TESOURA')
print('=-'*10)
if esc == resp:
    print('Empate')
elif resp == 1 and esc == 2:
    perdeu()
elif resp == 1 and esc == 3:
    venc()
elif resp == 2 and esc == 1:
    venc()
elif resp == 2 and esc == 3:
    perdeu()
elif resp == 3 and esc == 1:
    perdeu()
elif resp == 3 and esc == 2:
    venc()

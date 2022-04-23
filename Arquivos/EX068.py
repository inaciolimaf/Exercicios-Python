from random import randint
from time import sleep
print('-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)
vitoria=0
def vence():
    print('Você VENCEU!')
    print('Vamos jogar denovo')
def perdeu():
    print('Você PERDEU')
    if vitoria==0:
        print('Você não venceu nenhuma vez')
    elif vitoria==1:
        print('Você venceu uma vez')
    elif vitoria>1:
        print(f'GAME OVER! Você venceu {vitoria} vezes')
    else:
        print('ERRO')
while True:
    val=int(input('Digite um valor:'))
    esc=str(input('Par ou Ìmpar? [P/I]'))
    CompEsc=randint(1,10)
    total=CompEsc+val
    if total%2==0:
        resu='PAR'
    else:
        resu='ÍMPAR'
    sleep(1)
    print('-'*40)
    print(f'Você jogou {val} e o computador escolheu {CompEsc}. Total de {total} deu {resu}')
    print('-'*40)
    sleep(1)
    if esc in 'Pp':
        if resu=='PAR':
            vence()
            vitoria+=1
        elif resu=='ÍMPAR':
            perdeu()
            break
    elif esc in 'Ii':
        if resu=='PAR':
            perdeu()
            break
        elif resu=='ÍMPAR':
            vence()
            vitoria+=1
    else:
        print('DIGITE UM VALOR VÁLIDO')
    sleep(1)

from time import sleep
PedNum=False
PARAR=False
while not PARAR:
    if PedNum == False:
        Pri=int(input('Primeiro valor:'))
        Seg=int(input('Segundo valor:'))
        PedNum = True
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    Res=int(input('>>>> Qual é a sua opção?'))
    if Res==1:
        print('A soma entre {} e {} é {}'.format(Pri, Seg, Pri+Seg))
    elif Res==2:
        print('A multiplicação é {} e {} é {}'.format(Pri, Seg, Pri*Seg))
    elif Res==3:
        if Pri>Seg:
            print('O maior é {}'.format(Pri))
        elif Seg>Pri:
            print('O maior é {}'.format(Seg))
    elif Res==4:
        PedNum=False
    elif Res==5:
        PARAR=True
    else:
        print('Opção inválida')
    print('-='*20)
    sleep(1)

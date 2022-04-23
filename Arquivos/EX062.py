print('Gerador de P.A')
print('=-'*20)
pri=int(input('Primeiro termo: '))
r=int(input('Razão:'))
termo=pri
c=0
mais=0
while c<11+mais:
    print(termo, end='')
    if c==10+mais:
        print('.', end='')
    else:
        print(', ', end='')
    if c == 10 + mais:
        outra = int(input('\nQuantos termos você que mostrar a mais?'))
        mais += outra
    c+=1
    termo+=r



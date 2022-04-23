print('Gerador de P.A')
print('=-'*20)
pri=int(input('Primeiro termo: '))
r=int(input('Razão:'))
termo=pri
c=0
while c<11:
    print(termo, end='')
    if c==10:
        print('.')
    else:
        print(', ', end='')
    c+=1
    termo+=r
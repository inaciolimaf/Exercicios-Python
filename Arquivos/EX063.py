print('-'*40)
print('SequÊncia de Fibonacci')
print('-'*40)
qnt=int(input('Quantos termos você quer mostrar?'))
pri=1
seg=2
c=0
while c<qnt:
    if c==0:
        print('{}, {}, '.format(pri, seg), end='')
    novo=pri+seg
    print('{}'.format(novo), end='')
    if c==qnt-1:
        print('.')
    else:
        print(', ', end='')
    pri=seg
    seg=novo

    c+=1
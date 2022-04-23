total=0
c=False
resp=0
while c==False:
    soma=int(input('Digite um número[999 para parar]:'))

    if soma==999:
        c=True
    else:
        total += soma
        resp+=1
print('Você digitou {} números e a soma é {}'.format(resp, total))
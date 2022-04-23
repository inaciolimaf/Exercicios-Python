from random import randint
jogos=int(input('Quantos números você quer que eu sorteie?'))
n=[]
lista=[]
torf=True
for i in range(1,jogos+1):
    while len(lista)<6:
        n.append(randint(1,61))
        if n.count(n)==0:
            lista+=n
        n.clear()
    lista.sort()
    print(f'Jogo {i}: {lista}')
    lista.clear()

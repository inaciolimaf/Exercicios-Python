from random import randint
from operator import itemgetter
print('Valores sorteados:')
dicionario={'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 'Jogador 3': randint(1,6), 'Jogador 4': randint(1,6)}
for k,v in dicionario.items():
    print(f'O {k} tirou {v} no dado')
ordem=sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for j,v in enumerate(ordem):
    print(f'Em {j+1}º lugar:{v[0]} com {v[1]} pontos')
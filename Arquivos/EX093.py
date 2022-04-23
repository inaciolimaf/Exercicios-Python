dicionario={}
total=0
gols=[]
dicionario['Nome']=str(input('Nome de Jogador:'))
npartidas=int(input('Quantas partidas Zico jogou?'))
for n in range(0,npartidas):
    total+=npartidas
    gols.append(int(input('Quantos gols?:')))
dicionario['Gols']=gols
dicionario['Total']=total
print('-='*40)
print(dicionario)
for a, b in dicionario.items():
    print(f'O campo {a} tem o valor {b}')
print('-='*40)
print(f'O jogador {dicionario["Nome"]} jogou {len(dicionario["Gols"])} partidas.')
for c in range(0, len(dicionario["Gols"])):
    print(f'     Na partida {c+1}, fez {dicionario["Gols"][c]}')
print(f'Foi um total de {total} gols')
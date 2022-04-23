dicionario={}
junto=[]
gols=[]
cont=0
total=0
while True:
    dicionario['Nome']=str(input('Nome de Jogador:'))
    npartidas=int(input(f'Quantas partidas {dicionario["Nome"]} jogou?'))
    for n in range(0,npartidas):
        gols.append(int(input('Quantos gols?:')))
    dicionario['Gols']=gols[:]
    for e in gols:
        total+=e
    gols.clear()
    dicionario['Total']=total
    total=0
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    junto.append(dicionario.copy())
    dicionario.clear()
    if resp=='N':
        break
    print('-='*40)
print(junto)
print('Cod  Nome         Gols                 Total')
for d,e in enumerate(junto):
    print(f'{d+1:<5}', end='')
    cont=0
    for b,c in e.items():
        if cont==0:
            print(f'{c:<13}', end='')
        elif cont==1:
            c=str(c)
            print('{:<21}'.format(c), end='')
        elif cont==2:
            print(f'{c}', end='')
        cont+=1
    print()
while True:
    lugar=int(input('Mostar dados de qual jogador? (999n para parar)'))-1
    if lugar==998:
        break
    print(f'Levantamento do jogador: {junto[lugar]["Nome"]}')
    for n in range(0,len(junto[lugar]['Gols'])):
        print(f'No jogo {n+1} fez {junto[lugar]["Gols"][n]}')
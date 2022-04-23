nota=[]
lnome=[]
notasep=[]
tempnota=[]
while True:
    nome=str(input('Nome:'))
    nota1=int(input('Nota 1:'))
    nota2=int(input('Nota 2:'))
    tempnota.append(nota1)
    tempnota.append(nota2)
    notasep.append(tempnota[:])
    media=(nota1+nota2)/2
    lnome.append(nome)
    nota.append(media)
    tempnota.clear()
    resp=str(input('Quer continuar:')).strip().upper()[0]
    if resp=='N':
        break
print('No.  NOME                MÉDIA')
for i in range(0, len(lnome)):
    print(f'{i+1: <5}', end='')
    print(f'{lnome[i]: <20}', end='')
    print(f'{nota[i]}', end='')
    print()
while True:
    alun=int(input('Mostrar notas de qual aluno? [999 para interomper]'))
    if alun==999:
        break
    if alun>len(lnome):
        print('Valor inválido.')
    else:
        print(f'As notas de {lnome[alun-1]} são {notasep[alun-1]}')
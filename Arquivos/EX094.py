pessoas={}
contpes=contmul=0
sexo=[]
nome=[]
idade=[]
while True:
    nome.append(str(input('Nome:')))
    sexo1=str(input('Sexo: [M/F]')).strip().upper()[0]
    while True:
        if sexo1 not in 'MF':
            sexo1=str(input('VALOR INVÁLIDO: TENTE NOVAMENTE. Sexo: [M/F]')).strip().upper()[0]
        else:
            sexo.append(sexo1)
            if sexo1=='F':
                contmul+=1
            break
    idade.append(int(input('Idade:')))
    resp=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    contpes+=1
    if resp in 'N':
        break
pessoas['Nome']=nome
pessoas['Sexo']=sexo
pessoas['Idade']=idade
print('-='*30)
if contpes==1:
    print('Ao todo temos apenas uma pessoa cadastrada.')
else:
    print(f'Ao todo temos {contpes} pessoas cadastradas.')
media=0
for i in pessoas['Idade']:
    media+=i
media=media/len(pessoas['Idade'])
print(f'A media de idade é {media:.2f}')
if contmul==1:
    print(f'Ao todo temos apenas uma mulher cadatrada')
else:
    print(f'Ao todo temos {contmul} mulheres cadastradas')
print('Pessoas com nota acima da média.')
for j in range(0,len(pessoas['Idade'])):
    if pessoas['Idade'][j]>media:
        print(f'nome = {pessoas["Nome"][j]}; '
              f'idade = {pessoas["Idade"][j]};'
              f'sexo = {pessoas["Sexo"][j]}')
print()

dados=[]
comp=[]
maior=menor=regist=0
while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    if len(comp)==0:
        maior=menor=dados[1]
    else:
        if dados[1]>maior:
            maior=dados[1]
        elif dados[1]<menor:
            menor=dados[1]
    comp.append(dados[:])
    dados.clear()
    cont=str(input('Deseja continuar:')).upper().strip()[0]
    if cont=='N':
        break
    regist+=1
print(f'Ao todo, você cadastrou {len(comp)} pessoas')
print(f'O maior peso foi de {maior}. Peso de: ',end='')
for p in comp:
    if p[1]==maior:
        print(f'{p[0]}, ', end='')
print(f'\nO menor peso foi de {menor}. Pese de: ', end='')
for p in comp:
    if p[1]==menor:
        print(f'{p[0]}, ', end='')
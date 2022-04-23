tupla=(int(input('Digite um número:')),
       int(input('Digite outro número:')),
       int(input('Digite mais número:')),
       int(input('Digite o último número:')))
print(f'Você digitou os valores: {tupla}')
numnove=tupla.count(9)
if numnove==0:
    print('Nenhum número 9')
else:
    if numnove == 1:
        print('O número 9 só aparece uma vez')
    elif numnove>1:
        print(f'O numéro 9 aparece {numnove} vez')
num=tupla.count(3)
if num==0:
    print('O número 3 não aparece.')
else:
    num=tupla.index(3)
    print(f'O número 3 aparece na {num+1}° posição')
ntupla=(tupla[0]%2, tupla[1]%2, tupla[2]%2, tupla[3]%2)
ntuplacont=ntupla.count(0)
if ntuplacont==0:
    print('Nenhum número par')
elif ntuplacont==1:
    print('1 número par')
elif ntuplacont>1:
    print(f'{ntuplacont} números pares')
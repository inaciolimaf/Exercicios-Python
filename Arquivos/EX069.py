print('-'*40)
print('CADASTRE UMA PESSOA'.center(40))
print('-'*40)
NIdade=NMacho=NMulher=0
while True:
    idade=int(input('Idade:'))
    sexo=str(input('Sexo: [M/F]')).strip().upper()[0]
    cont=str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print('-'*40)
    if idade > 18:
        NIdade += 1
    if sexo=='M':
        NMacho+=1
    if sexo=='F' and idade<20:
        NMulher+=1
    if cont == 'N':
        break
if NIdade==0:
    print('Nenhuma pessoa com mais de 18 anos.')
elif NIdade==1:
    print('1 pessoa com mais de 18 anos.')
elif NIdade>1:
    print(f'{NIdade} pessoas com mais de 18 anos')
if NMacho==0:
    print('Nenhum homem cadastrado.')
elif NMacho==1:
    print('1 homem cadastrado.')
elif NMacho>1:
    print(f'{NMacho} homens cadastrados.')
if NMulher==0:
    print('E não temos nenhuma mulher com menos de 20 anos.')
elif NMulher == 1:
    print('Temos uma mulher com menos de 20 anos.')
elif NMulher>1:
    print(f'Temos {NMulher} com menos de 20 anos.')

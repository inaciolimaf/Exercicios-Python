somaID=0
homEsc=0
homEscId=0
mulEsc=0
for num in range(1,5):
    print('{:=^30}'.format(' {}° pessoa '.format(num)))
    nome=str(input('Nome:'))
    idade=int(input('Idade:'))
    sexo=str(input('Sexo [M/f] :'))
    if sexo=='F' and idade<=20:
        mulEsc+=1
    elif sexo== 'M' and idade>homEscId:
        homEscId=idade
        homEsc=nome
    somaID+= idade
print('A média de idade do grupo é de {} anos.'.format(somaID/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(idade, nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulEsc))

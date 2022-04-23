maior=1001
menor=0
respconti='S'
contvezes=0
total=0
while respconti in 'Ss':
    num=int(input('Digite um número:'))
    if contvezes==0:
        maior=num
        menor=num
    elif num>maior:
        maior=num
    elif num<menor:
        menor=num
    contvezes+=1
    total+=num
    respconti=str(input('Quer continuar? [S/N]'))
print('Você digitou {} números e a media foi {}'.format(contvezes, total/contvezes))
print('O maior valor foi {} e menor foi {}'.format(maior, menor))

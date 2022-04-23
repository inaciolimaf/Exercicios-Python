lista={}
lista['Nome'] = str(input('Nome:'))
lista['Media'] = float(input(f'Média de {lista["Nome"]}:'))
print('-='*30)
if lista['Media']<=6:
    lista['Situação']= 'Reprovado'
elif 7>lista['Media']>6:
    lista['Situação']= 'Recuperação'
elif lista['Media']>=7:
    lista['Situação']= 'Aprovado'
for itens, key in lista.items():
    print(f'{itens} é igual a {key}')
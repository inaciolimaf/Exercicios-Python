from datetime import date
dicionario={}
dicionario['Nome']=str(input('Nome:'))
nasc=int(input('Ano de nascimento:'))
dicionario['Idade']=date.today().year-nasc
carteira=int(input('Carteira de trabalho (0 não tem):'))
dicionario['Carteira']=carteira
if carteira!=0:
    dicionario['Contratação']=int(input('Ano de Contratação:'))
    dicionario['Salário']=int(input('Salário: R$'))
    dicionario['Aposentadoria']=dicionario['Idade']+((dicionario['Contratação']+35)-date.today().year)
for r,v in dicionario.items():
    print(f'{r} tem o valor de {v}')
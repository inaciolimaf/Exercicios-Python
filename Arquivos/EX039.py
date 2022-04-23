from datetime import date
nasc=int(input('Ano de nascimento:'))
AnoAtual=date.today().year
idade=AnoAtual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, AnoAtual))
if idade==18:
    print('Você já pode se alistar.')
elif idade>18:
    print('Você já deveria tem se alistado há {} anos'.format(idade-18))
else:
    print('Ainda faltam {} anos para você se alistar'.format(18-idade))
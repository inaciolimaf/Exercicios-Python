from datetime import date
AnoNas=int(input('Ano de nascimento:'))
AnoAtu= date.today().year
idade= AnoAtu-AnoNas
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Classificação: MIRIM')
elif idade<=14:
    print('Classificação: INFANTIL')
elif idade<=19:
    print('Classificação: JUNIOR')
elif idade<=25:
    print('Classificação: SÊNIOR')
elif idade>25:
    print('Classificação: MASTER')
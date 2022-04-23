Dist=float(input('Qual foi a distância?'))
if Dist<=200:
    print('O preço da passagem será de R${:.2f}'.format(Dist*0.5))
else:
    print('O preço da passagem será de R${:.2f}'.format(Dist*0.45))
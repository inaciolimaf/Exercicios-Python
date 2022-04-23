from datetime import date
Resp = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if Resp == 0:
    Anoerad = str(date.today())
    Ano=int(Anoerad[0:4])
    if Ano%4 ==0:
        print('O ano {} é BISSEXTO'.format(Ano))
    else:
        print('O ano {} NÃO é BISSEXTO'.format(Ano))
else:
    if Resp%4==0:
        print('O ano {} é BISSEXTO'.format(Resp))
    else:
        print('O ano {} é BISSEXTO'.format(Resp))
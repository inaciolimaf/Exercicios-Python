Dias=int(input('Quantos dias alugados?'))
Km=float(input('Quantos quilometros foram rodados?'))
PDias=float(input('Qual é o custo por um dia de uso?'))
PKm=float(input('Qual é o custo por quilometro rodado?'))
print('O total a pagar é {:.2f}'.format(PDias*Dias+PKm*Km))
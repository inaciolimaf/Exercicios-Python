Velocidade=int(input('Qual é a velocidade do carro?'))
if Velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${}'.format((Velocidade-80)*7))
print('Tenha um bom dia e dirija com segurança')
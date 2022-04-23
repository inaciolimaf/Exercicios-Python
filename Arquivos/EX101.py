from datetime import date
def vot(ano):
    idade=date.today().year-ano
    if idade<18:
        return 'NÃO VOTA'
    elif idade<63:
        return 'VOTO OBRIGATÓRIO'
    elif idade>63:
        return 'VOTO OPICIONAL'

ano=int(input('Em que ano você nasceu?'))
print(f'Situação: {vot(ano)}')
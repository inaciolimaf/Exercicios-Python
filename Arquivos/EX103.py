def jog(joga='<desconhecido>', gols=0):
    print(f'O jogador {joga} fez {gols} gols no campeonato')


jogador=str(input('Nome do jogador:'))
gols=str(input('Gols do jogador:'))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if jogador.strip()=='':
    jog('<desconhecido>',gols)
else:
    jog(jogador,gols)
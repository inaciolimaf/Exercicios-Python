times= ('Flamengo','Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 	'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians',
        'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 ultimos são {times[-4:]}')
print(f'Lista em ordem alfabética: {sorted(times)}')
print(f'O flamengo está na posição {times.index("Flamengo")+1}')
pri = float(input('Primeira nota:'))
seg = float(input('Segunda nota:'))
media = (pri+seg)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(pri, seg, media))
if media>7:
    print('O aluno foi APROVADO')
elif media>5 and media<7:
    print('O aluno está de recuperação')
else:
    print('O aluno foi reprovado')
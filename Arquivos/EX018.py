import math
angulo=float(input('Digite o ângulo que você deseja:'))
RadAngulo=math.radians(angulo)
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, math.sin(RadAngulo)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(RadAngulo)))
print('O angulo de {} tem a tangente {:.2f}'.format(angulo, math.tan(RadAngulo)))
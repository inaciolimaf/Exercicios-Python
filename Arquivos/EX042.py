pri = float(input('Primeiro segmento:'))
seg = float(input('Segundo segmento:'))
ter = float(input('Terceiro segmento:'))
if pri==seg==ter:
    form='EQUILÁTERO'
elif pri==seg or pri==ter or seg==ter:
    form='ISÓCELES'
else:
    form='ESCALENO'
if pri<seg+ter and seg<pri+ter and ter<pri+seg:
    print('Os segmentos acima PODEM FORMAR um triângulo {}'.format(form))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
largura = float(input('Digite a largura da parede em metros:'))
altura = float(input('Digite a altura da parede em metros:'))
rendimeto = float(input('Usando 1l de tinta é possível pinta quanto m² de parede?'))
area = largura*altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(area/rendimeto))

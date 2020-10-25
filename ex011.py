"""
    curso Python 3 - Exercício Python #011
    crie um programa que leia a largura e altura de uma parede em metros, calcule a sua area, 
    quantidade de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta 2m²
    25.10.2020 - Felipe Ferreira de Aguiar
"""

larg = float(input('Digite a largura da parede em metros '))
altu = float(input('Digite a altura da parede em metros '))
area = larg * altu
litr = area / 2
gala = area / 0.52
print('A area total é {:.2f} m² e será necessário {:.2f} litros'.format(area, litr, gala), end='')
print(' ou {:.2f} galões de tinta para pintá-la'.format(gala))

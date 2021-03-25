"""
    curso Python 3 - Exercício Python #017
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
    triangulo retangulo, calcule e mostre o comprimento da hipotenusa
    25.03.2021 - Felipe Ferreira de Aguiar
"""

from math import hypot
cateto_o = float(input('Digite o valor do cateto oposto '))
cateto_a = float(input('Digite o valor do cateto adjacente '))
print('O cateto oposto é {:.2f}, o cateto adjacente é {:.2f} e a hipotenusa {:.2f}'.format(cateto_o, cateto_a, hypot(cateto_a, cateto_o)))

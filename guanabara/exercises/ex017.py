"""
    curso Python 3 - Exercício Python #017
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
    triangulo retangulo, calcule e mostre o comprimento da hipotenusa
    25.03.2021 - Felipe Ferreira de Aguiar
"""

from math import hypot
cateto_o = float(input('Digite o valor do cateto oposto '))
cateto_a = float(input('Digite o valor do cateto adjacente '))
print(f'O cateto oposto é {cateto_o:.2f}, o cateto adjacente é {cateto_a:.2f} e a hipotenusa {hypot(cateto_o, cateto_a):.2f}')

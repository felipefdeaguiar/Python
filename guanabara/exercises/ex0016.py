"""
    curso Python 3 - Exercício Python #016
    Crie um programa que leia um numero real qualquer pelo teclado e mostre na teclado 
    a sua porção inteira
    25.03.2021 - Felipe Ferreira de Aguiar
"""
import math
num = float(input('Digite um numero qualquer '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))


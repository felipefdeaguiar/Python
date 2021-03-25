"""
    curso Python 3 - Exercício Python #018
    Faça um programa que leia um angulo qualquer e mostre na tela seu seno, cosseno e tangente desse angulo
    25.03.2021 - Felipe Ferreira de Aguiar
"""

import math
ang = float(input('Digite o valor do angulo '))
sen = math.sin(ang)
con = math.cos(ang)
tan = math.tan(ang)
print(f'\nO angulo digitado foi {ang:.2f}º\nResultado: Seno {sen:.2f}º, Coseno {con:.2f}º e Tangente {tan:.2f}º\n')

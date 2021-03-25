"""
    curso Python 3 - Exercício Python #018
    Faça um programa que leia um angulo qualquer e mostre na tela seu seno, cosseno e tangente desse angulo
    25.03.2021 - Felipe Ferreira de Aguiar
"""

import math
ang = float(input('Digite o valor do angulo '))
sen = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'\nO angulo digitado foi {ang:.2f}\nResultado: Seno {sen:.2f}, Cosseno {con:.2f} e Tangente {tan:.2f}\n')

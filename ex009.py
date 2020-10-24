"""
    curso Python 3 - Exercício Python #009
    crie um programa que leia um numero inteiro e mostre sua tabuada até 10
    24.10.2020 - Felipe Ferreira de Aguiar
"""

num = int(input('Digite um numero inteiro para ver a sua tabuada até 10 '))
tab_1 = num * 1
tab_2 = num * 2
tab_3 = num * 3
tab_4 = num * 4
tab_5 = num * 5
tab_6 = num * 6
tab_7 = num * 7
tab_8 = num * 8
tab_9 = num * 9
tab_10 = num * 10
print('==============')
print('{} x 01 = {}\n{} x 02 = {}\n{} x 03 = {}\n'.format(num, tab_1, num, tab_2, num, tab_3), end='')
print('{} x 04 = {}\n{} x 05 = {}\n{} x 06 = {}\n'.format(num, tab_4, num, tab_5, num, tab_6), end='')
print('{} x 07 = {}\n{} x 08 = {}\n{} x 09 = {}\n'.format(num, tab_7, num, tab_8, num, tab_9), end='')
print('{} x 10 = {}\n'.format(num, tab_10), end='')
print('==============')

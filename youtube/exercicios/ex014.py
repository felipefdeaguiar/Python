"""
    curso Python 3 - Exercício Python #014
    crie um programa que converta a temperatura em graus ºC para ºF 
    25.10.2020 - Felipe Ferreira de Aguiar
"""

#! a formula pode ser também (temp_c * 1.8) + 32

temp_c = float(input('Digite a temperatura em graus Celsius '))
temp_f = (( temp_c * 9 ) / 5) + 32
print('No seu ambiente está {:.2f}º Celsius ou {:.2f}º Fahrenheit'.format(temp_c, temp_f))

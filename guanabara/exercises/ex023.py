"""
    curso Python 3 - Exercício Python #023
    Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos saparados
    13.04.2021 - Felipe Ferreira de Aguiar
"""

num = input('Digite um valor de 1000 à 9999 ')
if num.isdigit():
    print(f'\nO valor digitado foi {num}\nSua milhar é {num[0]}\nSua centena é {num[1]}\nSua dezena é {num[2]}\nSua unidade é {num[3]}\n')
else:
    print('Digite um numeral correto')

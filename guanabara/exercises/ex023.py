"""
    curso Python 3 - Exercício Python #023
    Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos saparados
    13.04.2021 - Felipe Ferreira de Aguiar
"""

num = input('Digite um valor de 0 à 9999 ')
if num.isdigit():
    n = int(num)
    u = n // 1 % 10
    d = n // 10 % 10
    c = n // 100 % 10
    m = n // 1000 % 10
    print(f'\nO valor digitado foi {num}\nSua milhar é {m}\nSua centena é {c}\nSua dezena é {d}\nSua unidade é {u}\n')
else:
    print('Digite um numero correto')

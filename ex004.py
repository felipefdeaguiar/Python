"""
    curso Python 3 - Exercício Python #004
    crie um programa que leia algo do teclado e mostre na tela seu tipo primitivo e todas as informações
    19.10.2020 - Felipe Ferreira de Aguiar
"""

x = input('Digite algo aqui ')
print('Qual é o seu tipo primitivo {}'.format(type(x)))
print('È um número ? {}'.format(x.isnumeric()))
print('É alfabeto ? {}'.format(x.isalpha()))
print('É alphanúmerico ? {}'.format(x.isalnum()))
print('Está em maiusculo ? {}'.format(x.isupper()))
print('Está em minusculo ? {}'.format(x.islower()))
print('Só tem espaços ? {}'.format(x.isspace()))
print('Está captalizada ? {}'.format(x.istitle()))

"""
    curso Python 3 - Exercício Python #012
    crie um programa que leia o preço de um produto e mostre seu novo preço com desconto de 5 %
    25.10.2020 - Felipe Ferreira de Aguiar
"""

price = float(input('Digite o valor do produto R$ '))
off = ( 5 / 100 ) * 100
des = ( price * off ) / 100
price_n = price - des
print('O valor do produto é R$ {:.2f}, com o desconto de {:.0f}%'.format(price, off), end='')
print(' o novo valor ficou em R$ {:.2f}'.format(price_n))

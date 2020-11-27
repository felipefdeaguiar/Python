"""
    curso Python 3 - Exercício Python #010
    crie um programa leia quanto dinheiro uma pessoa tem na carteira e mostre em outras moedas
    25.10.2020 - Felipe Ferreira de Aguiar
"""

BRL = float(input('Digite quanto você tem na carteira ? R$ '))
USD = BRL / 5.62
EUR = BRL / 6.66
GBP = BRL / 7.33
YEN = BRL / 0.054
print('Com BRL {:.2f}\nvocê pode comprar USD {:.2f}\n'.format(BRL, USD), end='')
print('você pode comprar EUR {:.2f}\nvocê pode comprar GBP {:.2f}\n'.format(EUR, GBP), end='')
print('você pode comprar YEN {:.2f}'.format(YEN))

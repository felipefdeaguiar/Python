"""
curso Python 3 - Exercício Python #006
crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
20.10.2020 - Felipe Ferreira de Aguiar
"""

n1 = float(input('Digite um valor '))
doble = n1 * 2
triple = n1 * 3
raiz = n1 ** (1/2)
print('O valor digitado foi {:.2f}\nSeu dobro é {:.2f}\n'.format(n1, doble), end='')
print('O triplo é {:.2f}\nE sua raiz quadrada é {:.2f}'.format(triple, raiz))

"""
    curso Python 3 - Exercício Python #007
    crie um algoritmo que leia as duas notas do aluno e mostre a sua média
    24.10.2020 - Felipe Ferreira de Aguiar
"""

n1 = float(input('Digite a sua primeira nota '))
n2 = float(input('Digite a sua segunda nota '))
avg = (n1 + n2) / 2
print('A sua primeira nota foi {:.1f} a nota segunda {:.1f}'.format(n1, n2), end='')
print(' e com média de {}'.format(avg))

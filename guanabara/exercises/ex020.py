"""
    curso Python 3 - Exercício Python #019
    Um professor quer sortear a ordem de apresentaçao dos seus quatro alunos,
    faça um programa que ajude ele, lendo o nome dos alunos e listando a ordem.
    25.03.2021 - Felipe Ferreira de Aguiar
"""

from random import sample
a1 = str(input('Digite o nome do aluno 1 '))
a2 = str(input('Digite o nome do aluno 2 '))
a3 = str(input('Digite o nome do aluno 3 '))
a4 = str(input('Digite o nome do aluno 4 '))
lista = sample([a1, a2, a3, a4], k=4)
print(f'A ordem da apresentação é {lista}')

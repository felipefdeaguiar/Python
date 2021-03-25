"""
    curso Python 3 - Exercício Python #019
    Um professor quer sortear um dos seus quatro alunos para apagar seu quadro,
    faça um programa que ajude ele, lendo o nome dos alunos e sorteano um.
    25.03.2021 - Felipe Ferreira de Aguiar
"""
import random
a1 = str(input('Digite o nome do aluno 1 '))
a2 = str(input('Digite o nome do aluno 2 '))
a3 = str(input('Digite o nome do aluno 3 '))
a4 = str(input('Digite o nome do aluno 4 '))
sorteador = random.choice([a1, a2, a3, a4])
print(f'O aluno sorteado foi o {sorteador}')

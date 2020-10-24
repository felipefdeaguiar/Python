"""
    curso Python 3 - Exercício Python #005
    crie um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor
    20.10.2020 - Felipe Ferreira de Aguiar
"""

n1 = int(input('Digite um numero inteiro '))
d = n1+1
a = n1-1
print('O numero inteiro digitado foi {}, seu sucessor é {} e antecessor é {}'.format(n1, d, a))
#print('O numero inteiro digitado foi {}, seu sucessor é {} e antecessor é {}'.format(n1, (n1+1), (n1-1)))

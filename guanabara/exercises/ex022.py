"""
    curso Python 3 - Exercício Python #022
    Faça um programa que leia o nome completo de uma pessoa e mostre:
    1) O nome com todas as letras maiusculas;
    2) O nome com todos as letras Minusculas;
    3) Quantas letras tem sem contar os espaços;
    4) Quantas letras tem o primeiro nome.
    13.04.2021 - Felipe Ferreira de Aguiar
"""

nome = input('Qual é o seu nome completo ')
print(f'\nO nome digitado foi {nome}')
print('Transformando em Maiusculo:',nome.upper())
print('Transformando em Minusculo:',nome.lower())
nome_1 = nome.replace(" ","")
print(f'A quantidade do nome completo são {len(nome_1)} caracteres')
nome_2 = nome.split()
print(f'A quantidade do primeiro nome são {len(nome_2[0])} caracteres\n')
#curso Python 3 - Aula 006 - tipos primitivos e saída de Dados
#Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python.
#18.10.2020 - Felipe Ferreira de Aguiar

number_1 = float(input('digite um número '))
number_2 = float(input('digite outro '))
sum = number_1 + number_2
print('A soma entre {} e {} vale {}'.format(number_1, number_2, sum))

#desafio 003 - crie um programa que leia dois numeros e mostre a soma entre eles.
number_1 = float(input('Qual o primeiro número? '))
number_2 = float(input('Qual o segundo número? '))
sum = number_1 + number_2
print('A soma de {} com {} é igual a {}'.format(number_1, number_2, sum))

#desafio 004 - crie um programa que leia o input do teclado e mostre na tela seu tipo primitivo e todas as informações
x = input('digite algo aqui! ')
print('Qual é o tipo primitivo digitado {}'.format(type(x)))
print('O que foi digitado é uma letra ? {}'.format(x.isalpha()))
print('O que foi digitado é alfanumérico ? {}'.format(x.isalnum()))
print('O que foi digitado é número ? {}'.format(x.isnumeric()))
print('O que foi digitado está em maiusculo ? {}'.format(x.isupper()))
print('O que foi digitado está em minusculo ? {}'.format(x.islower()))

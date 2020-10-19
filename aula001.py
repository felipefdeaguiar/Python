#curso de Python 3 - Mundo 1: Fundamentos
#https://www.youtube.com/playlist?list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6
#16.10.2020 - Felipe Ferreira de Aguiar

#escrever na tela
print('Olá, Mundo!')
print(7+4)
print('7'+'4')

#variaveis Fixas
nome = 'Felipe'
idade = 35
peso = 79.9
print(nome, idade, peso)

#variaveis por digitação na tela
nome = input('Qual é o seu nome? ')
idade = input('Qual a sua idade? ')
peso = input('Qual o seu peso? ')
print(nome, idade, peso)

#desafio 01
print('==== Desafio 01 ====')
nome = input('Qual o seu nome? ')
print('Ola', nome,'! Prazer em te conhecer')

#desafio 02
print('==== Desafio 02 ====')
dia = input('Qual dia voce nasceu? ')
mes = input('Qual mes voce nasceu? ')
ano = input('Qual ano voce nasceu? ')
print('Vocẽ nasceu em', dia, 'de', mes, 'de', ano, '. Correto ? ')

#desafio 03
print('==== Desafio 03 ====')
number_1 = float(input('Digite o primeiro numero '))
number_2 = float(input('Digite o segundo numero '))
soma = number_1 + number_2
print('A soma do números digitados é',soma)

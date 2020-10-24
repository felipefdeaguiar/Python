"""curso Python 3 - Aula 007 - Operadores Aritméticos
Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.
19.10.2020 - Felipe Ferreira de Aguiar
"""

number_1 = int(input('Digite um valor inteiro '))
number_2 = int(input('Digite outro valor inteiro '))
s = number_1 + number_2
m = number_1 * number_2
d = number_1 / number_2
di = number_1 // number_2
e = number_1 ** number_2
print('soma {} \nmultiplicação {} \ndivisão {:.2f} \n'.format(s, m, d), end='')
print('divisão inteira {}\npontência {}'.format(di, e))

#desafio 005 - crie um programa que leia um numero inteiro e mostre na tela seu sucessor e antecessor
n1 = int(input('Desafio 005 - Digite um numero inteiro '))
d = n1+1
a = n1-1
print('O numero inteiro digitado foi {}, seu sucessor é {} e antecessor é {}'.format(n1, d, a))

#desafio 006 - crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada
n1 = float(input('Desafio 006 - Digite um valor '))
doble = n1 * 2
triple = n1 * 3
raiz = n1 ** (1/2)
print('O valor digitado foi {:.1f}, seu dobro é {:.1f},'.format(n1, doble), end='')
print(' o triplo é {:.1f} e sua raiz quadrada é {:.1f}'.format(triple, raiz))

#desafio 007 - crie um programa que leia as notas do aluno, e calcule a sua média
n1 = float(input('Desafio 007 - Digite a sua primeira nota '))
n2 = float(input('Desafio 007 - Digite sua segunda nota '))
avg = (n1 + n2) / 2
print('A sua primeira nota foi {:.2f}, a segunda foi {:.2f}'.format(n1, n2), end='')
print(' e como media final {:.2f}'.format(avg))

#desafio 008 - crie um programa que leia em metros e exiba convertido em centimetros e milimetros
n1 = float(input('Desafio 008 - Digite os metros '))
ce = n1 * 100
mi = n1 * 1000
print('O valor convertido em cm é {:.0f} e em mm é {:.0f}'.format(ce, mi))

#desafio 009 - crie um programa que leia um numero inteiro e mostre sua tabuada
n1 = int(input('Desafio 009 - Digite um numero inteiro '))
tab_2 = n1 * 2
tab_3 = n1 * 3
tab_4 = n1 * 4
tab_5 = n1 * 5
tab_6 = n1 * 6
tab_7 = n1 * 7
tab_8 = n1 * 8
tab_9 = n1 * 9
tab_10 = n1 * 10
print('A tabuada até 10 é {},{},{},{},{},'.format(n1, tab_2, tab_3, tab_4, tab_5), end='')
print('{},{},{},{}e{}'.format(tab_6, tab_7, tab_8, tab_9, tab_10))

#desafio 010 - crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
#mostre quantos dolares ela pode comprar (cambio USD 3,27)
real = float(input('Desafio 010 - Digite quantos Reais voce tem na carteira '))
cambio = 3.27
usd = real / cambio
print('você tem na carteira BRL {:.2f} e pode comprar USD {:.2f} '.format(real, usd), end='')
print('com o cambio atual de {}'.format(cambio))

#desafio 011 - crie um programa que leia a largura e altura em metros de uma parede e calcule a sua
#area, e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta 2m²
largura = float(input('Desafio 011 - Digite em metros a largura da parede '))
altura = float(input('Digite em metros a altura da parede '))
area = largura * altura
tinta = area / 2
galao = tinta / 3.6
print('A area total da parede é {}m² e sera necessário {:.2f} '.format(area, tinta), end='')
print('litros de tinta para pinta-la ou {:.2f} galoes'.format(galao))

#desafio 012 - crie um programa que leia o preço do produto e mostre seu novo preço com 5% de desconto
preco = float(input('Desafio 012 - Qual o preço do produto? '))
desconto = (5 / 100) * 100
novo = (preco * desconto) / 100
preco_n = preco - novo
print('O com o desconto de {} % o novo preço será R$ {}'.format(desconto, preco_n))

#desafio 013 - crie um programa que leia o salario de um funcionario e mostre seu novo
#salario com 15% de aumento
salario = float(input('Qual o seu salario atual? '))
aumento = (15 / 100) * 100
novo = (salario * aumento) / 100
salario_n = salario + novo
print('O seu salário é R$ {:.2f}, com aumento de {:.0f} % '.format(salario, aumento), end='')
print('o seu novo salário é R$ {:.2f}, parabéns!'.format(salario_n))

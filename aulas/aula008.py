"""
    curso Python 3 - Aula 008 - Utilizando Módulos
    Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
    04.11.2020 - Felipe Ferreira de Aguiar
"""

#'from math import sqrt', outra forma de importar somente um modulo.
import math
num = int(input('Digite um numero inteiro '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#todo importar a biblioteca random e mostrar um numero inteiro aleatorio
import random
num = random.randint(1, 100)
print (num)

#todo desafio 014 - crie um programa que leia um numero real e mostre sua porção inteira
import math
real = float(input('Digite um numero real '))
conv = math.ceil(real)
print('O numero real digitado foi {} convertido para inteiro é {}'.format(real, conv))

#todo desafio 015 - crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule e mostre a sua hipotenusa
import math
cat_adj = float(input('Digite o valor do catero adjacente '))
cat_opt = float(input('Digite o valor do catero oposto '))
hipotenusa = math.hypot(cat_adj, cat_opt)
print('A hipotenusa é {:.2f}'.format(hipotenusa))

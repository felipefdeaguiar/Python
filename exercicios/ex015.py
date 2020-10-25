"""
    curso Python 3 - Exercício Python #015
    crie um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
    de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que custa R$ 60 a diaria
    e R$ 0,15 por KM rodado
    25.10.2020 - Felipe Ferreira de Aguiar
"""

name = input ('Qual o seu nome ? ')
day = int(input('Digite quantos dias voce ficou com o carro ? '))
km = float(input('Digite o quantidade de KM que voce rodou ? '))
t1 = day * 60
t2 = km * 0.15
cash = t1 + t2
print('=========')
print('diária R$ 60 x {} dias alugados = R$ {:.2f}'.format(day, t1))
print('KM R$ 0,15 x {:.2f} KM rodados = R$ {:.2f}'.format(km, t2))
print('=========')
print('{} o valor total a ser pago é R$ {:.2f}'.format(name, cash))

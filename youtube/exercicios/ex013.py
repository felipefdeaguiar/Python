"""
    curso Python 3 - Exercício Python #013
    crie um programa que leia o salario do funcionario e mostre seu novo com aumento
    25.10.2020 - Felipe Ferreira de Aguiar
"""
nome = input('Qual o seu nome ? ')
salario = float(input('Digite seu salario em R$ '))
aumento = float(input('Digite o aumento em % '))
percentual = ( aumento / 100 ) * 100
promocao = ( salario * percentual ) / 100
salario_n = salario + promocao
print('Salario atual R$ {:.2f} com o bonus de {:.2f} %'.format(salario , percentual), end='')
print(' o seu novo salario ficou em R$ {:.2f}\nParabéns {}!'.format(salario_n, nome))

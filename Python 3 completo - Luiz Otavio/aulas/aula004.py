"""
    7.12.2020 - Felipe Ferreira de Aguiar
    * Tipos de dados primitivos
    ? str = string (texto) 
    ? int = inteiro (123456)
    ? float = real (7.7)
    ? bool = logico (True or False)
"""

# função type retorna o tipo de dado
print('"Felipe" é um tipo', type('Felipe'))
print('"123456" é um tipo', type(123456))
print('"7.7" é um tipo', type(7.7))
print('"True" é um tipo', type(True))
print('"False" é um tipo', type(False))
print(10==10, type(10==10))

# ? Coverter um tipo para outro tipo " print(type(int('123456'))) "
print("'123456' é um tipo", type('123456'),'Convertido para', end=' ')
print(type(float('123456')))

# Exercicio escrever na tela o seu nome, idade, altura e se voce é maior de 18 anos
print('Felipe', type('Felipe'))
print(35, type(35))
print(1.79, type(1.79))
print(35 > 18, type (35 > 18))

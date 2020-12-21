"""
    16.12.2020 - Felipe Ferreira de Aguiar
    Formatando valores em Python

    :s (strings)
    :d (int)
    :f (float)
    :.(numero)f - Quantidade de casas decimais
    : (caractere) (> ou < ou ^) (Quantidade) (tipo - s, d, f)

    > - Esquerda
    < - Direita
    ^ - Meio

"""

# ! Adicação de zeros a esquerda
num_1 = 1
print(f'{num_1:0>10}')

# ! Adicação de zeros a direita
num_1 = 1
print(f'{num_1:0<10}')

# ! Formatando para numero virar float
num_1 = 1
print(f'{num_1:.2f}')

# ! Formatando para numero virar float e dez casas decimais à esquerda
num_1 = 1
print(f'{num_1:0>10.2f}')

# ! Formatando strings com nome no meio e cerquilhas até 30 caracteres
nome = 'Felipe Aguiar'
print(f'{nome:#^30}')

# ! Formatando strings para caracteres minusculos
nome = 'Felipe Aguiar'
print(nome.lower())

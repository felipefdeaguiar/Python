"""
    11.12.2020 - Felipe Ferreira de Aguiar
    Documentação e funções built-in
"""

# ! Validação / Check do input convertendo em inteiro

num_1 = input('Digite um numero inteiro ')
num_2 = input('Digite outro numero inteiro ')

if num_1.isdigit() and num_2.isdigit():
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(f'A soma do {num_1} com {num_2} é igual a {(num_1) + (num_2)}')
else:
    print('Favor verficar o que foi digitado')


# ! Funções prontas
# ? Docs Python - https://docs.python.org/pt-br/3/library/stdtypes.html
# ? GitHub Luiz Otavio - https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########
 
# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
 
# False
print(is_number('123a'))  # False

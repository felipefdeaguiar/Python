"""
    15.12.2020 - Felipe Ferreira de Aguiar
    Pass e Ellipsis
"""

# ! (Pass) utilizado para depois programar "placeholders" e não gerar erro no código

valor = False

if valor:
    pass
else:
    print('Vou escrever se valor for False (Pass)')

# ! Ellipsis (...) outra forma de gerar um "placeholders" 

valor = False

if valor:
    ...
else:
    print('Vou escrever se valor for False (...)')

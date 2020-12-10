"""
    10.12.2020 - Felipe Ferreira de Aguiar
    Quantidade de caracter
"""

usuario = input('Qual o seu nome ? ')
validacao = len(usuario)

if validacao < 6:
    print('Você precisa digitar no minimo seis caracteres')
else:
    print('Voce foi cadastrado')



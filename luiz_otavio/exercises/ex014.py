"""
    23.12.2020 - Felipe Ferreira de Aguiar
    Manipulando Strings

    * Strings Indices
    * Fatiamento de Strings
    * Funcões built-in len, abs, type, print

    Documentação da aula abaixo:
    https://docs.python.org/3/library/functions.html 
    https://docs.python.org/3/library/stdtypes.html

"""

# ! indice positivos [p = 0 , y = 1 .... 2 = 8]
texto = 'python s2'
print(texto[8])

# ! indice negativos -[987654321]
texto = 'python s2'
print(texto[-9])

# ! teste de print para ocultar ultimo caracter
url = 'www.google.com/'
print(url[:-1])

# ! print de um caracter especifico ao outro, porem o ultimo indice não é incluido
str = 'Felipe Aguiar'
nova_str = str[2:6]
print(nova_str)



"""
    05.01.2021 - Felipe Ferreira de Aguiar
    Interando Strings com While
"""

# ? índices
# ? 0123456789.......................33

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0

while contador < 10:
    print(frase[contador], contador)
    contador = contador + 1

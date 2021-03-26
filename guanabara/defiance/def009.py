"""
    curso Python 3 - Aula 009 - Utilizando Módulos
    Nessa aula, manipulando cadeias de texto
    26.03.2021 - Felipe Ferreira de Aguiar
"""

#! Indice aprendendo como o computador aloca a memória
#! frase = 'Curso em Video Python'
#! indice = 0=C, 1=u, 2=r, ..., h=18, o=19 e n=20

#! Fatiamento de Strings
frase = 'Curso em Video Python'
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#! Análise de strings
frase = 'Curso em Video Python'
print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))

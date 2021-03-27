"""
    curso Python 3 - Aula 009 - Utilizando Módulos
    Nessa aula, manipulando cadeias de texto
    26.03.2021 - Felipe Ferreira de Aguiar
"""

#! Indice aprendendo como o computador aloca a memória
#! frase = 'Curso em Video Python'
#! indice = 0=C, 1=u, 2=r, ..., h=18, o=19 e n=20

#! Fatiamento de strings
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
print('Curso' in frase)

#! Transformação de strings
frase = 'Curso em Video Python'
print(frase,'"Frase 1 Original"')
print(frase.replace('Python', 'Android'),'"Substituição de uma palavra"')
print(frase.upper(),'"Transformação da string para Maiusculas"')
print(frase.lower(),'"Transformação da String para Minusculas"')
print(frase.capitalize(),'"Somente a primeira letra fica Maiusculas"')
print(frase.title(),'"Todas as letras iniciais das palavras ficam Maiusculas"\n')
frase_2 = '   Aprenda Python'
print(frase_2,'"Frase 2 Original"')
print(frase_2.strip(),'"Remoção dos espaços vazios no inicio da String"')
print(frase_2.rstrip(),'"Remoção dos espaços vazios no fim da String"')
print(frase_2.lstrip(),'"Remoção dos espaços da esquerda da String"')

#! Divisão de strings
frase = 'Curso em Video Python'
print(frase,'"Frase 1 Original"')
print(frase.split(),'"Divisão da frase em nomes separados em listas"')

#! Junção de strings
frase = 'Curso em Video Python'
print(frase,'"Frase 1 Original"')
print('-'.join(frase),'"Junção de Strings"')
print(''.join(frase),'"Junção de Strings"')

#! Escrevendo um texto grande em Python com """
print("""Welcome Welcome Welcome Welcome Welcome Welcome Welcome Welcome
Welcome Welcome Welcome Welcome Welcome Welcome Welcome Welcome Welcome
Welcome Welcome Welcome Welcome Welcome Welcome Welcome Welcome Welcome
Welcome Welcome Welcome Welcome Welcome""")

#todo 

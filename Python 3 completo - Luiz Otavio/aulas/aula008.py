"""
    7.12.2020 - Felipe Ferreira de Aguiar
    Aula de entrada de dados do usuário
"""

nome = input('Qual o seu nome ? ')
idade = int(input('Qual a sua idade ? '))
ano_nascimento = 2020 - idade

# ! Metodo I
print('')
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')

# ! Metodo II
print('')
print('{} tem {} anos e nasceu em {}'.format(nome, idade, ano_nascimento))

# ? Metodo Transformação variavel idade de str para int
# ? idade = input('Qual a sua idade ? ')
# ? ano_nascimento = 2020 - int(idade)
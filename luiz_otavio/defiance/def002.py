"""
    15.12.2020 - Felipe Ferreira de Aguiar
    Exercícios Propostos
"""

"""
    Ex 001
    Faça um programa que peça ao usuário para digitar um numero inteiro, informe se esse 
    número é par ou impar, e caso o usuário digite um numero que não seja inteiro informe a ele
"""

"""
    Ex 002
    Faça um programa que pergunte a hora ao usuário, e baseado nisso exiba a saudação apropriada,
    ex: Bom dia (0-11), Boa Tarde (12-17) e Boa Noite (18-23)
"""

"""
    Ex 003
    Faça um programa que leia o nome do usuário, se o nome tiver 4 letras ou menos escreva seu nome
    é muito curto, se tiver entre 5 e 6 escreva seu nome é normal, e se tiver acima disso escreva seu nome é grande
"""

# todo Ex 001

num_1 = input('Digite um numero inteiro : ')

if num_1.isdigit():
    num_1 = int(num_1)
    teste = num_1 % 2
    if teste == 0:
        print(f'O valor digitado {num_1} é um numero inteiro e é Par')
    else:
        print(f'O valor digitado {num_1} é um numero inteiro e é Impar')
else:
    print('O valor digitado não foi um numero inteiro !')

# todo Ex 002

hora = int(input('Digite a hora que está no seu relógio : '))

if hora <= 11:
    print('Ola tenha um Bom Dia!')
elif hora >=12 and hora < 18:
    print('Ola tenha uma boa tarde')
elif hora >=18 and hora <=23:
    print('Ola tenha uma boa noite')
else:
    print('Veja o valor da hora digitado')

# todo Ex 003

name = input('Digite seu primeiro nome : ')
validacao = len(name)

if validacao <= 4 and validacao >0:
    print('')
    print(f'O tamanho do seu nome é "curto" tem {validacao} caracteres')
    print('')
elif validacao <=6 and validacao >=5:
    print('')
    print(f'O tamanho do seu nome é "normal" tem {validacao} caracteres')
    print('')
elif validacao >=6:
    print('')
    print(f'O tamanho do seu nome é "gigante" tem {validacao} caracteres ')
    print('')
elif validacao <= 0:
    print('')
    print(' Espertinho(a) voce não digitou nada')
    print('')
"""
    15.12.2020 - Felipe Ferreira de Aguiar
    Exercícios Propostos
"""

"""
    Ex 001
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro, informe que não é um número inteiro.
"""

"""
    Ex 002
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
    descrito, exiba a saudação apropriada. Ex. 
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
    Ex 003
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
    menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
    "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
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

hora = input('Digite a hora que está no seu relógio : ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('O valor digiado deve estar entre 0 ate 23 horas')
    else:
        if hora <= 11:
            print('Bom dia!')
        elif hora <=17:
            print('Boa tarde')
        else:
            print('Boa noite')    
else:
    print('Isso não é um valor certo')

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


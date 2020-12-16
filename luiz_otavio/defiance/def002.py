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

num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    
    if num % 2 == 0:
        print(f'O numero {num} é par')
    else:
        print(f'O numero {num} é impar')
     
else:
    print('Isso não é um numero inteiro')

# todo Ex 002

hora = input('Digite a hora que está no seu relógio : ')

if hora.isdigit():
    hora = int(hora)
    
    if hora > 0 and hora < 12:
        print(f'ola são {hora} horas, tenha um bom dia')
    elif hora >= 12 and hora < 18:
        print(f'ola são {hora} horas, tenha uma boa tarde')
    elif hora >= 18 and hora < 24:
        print(f'ola são {hora} horas, tenha uma boa noite')
    else:
        print('O valor digitado deve estar entre 0 e 23 horas')

else:
    print('O valor digitado não foi um valor inteiro / digito')

 
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
elif validacao == 0:
    print('')
    print(' Espertinho(a) voce não digitou nada')
    print('')

# ! Soluções do Luiz Otavio

# todo Ex 001

# numero_inteiro = input('Digite um número inteiro: ')
#
# if not numero_inteiro.isdigit():
#     print('Isso não é um número inteiro')
# else:
#     numero_inteiro = int(numero_inteiro)
#
#     if not numero_inteiro % 2 == 0:
#         print(f'{numero_inteiro} é ímpar')
#     else:
#         print(f'{numero_inteiro} é par')


# todo Ex 002

# horario = input('Digite um horário (0-23): ')
#
# if horario.isdigit():
#     horario = int(horario)
#
#     if horario < 0 or horario > 23:
#         print("Horário deve estar entre 0 e 23")
#     else:
#         if horario <= 11:
#             print('Boa dia!')
#         elif horario <= 17:
#             print('Boa tarde!')
#         else:
#             print('Boa noite!')
# else:
#     print("Por favor, digite um horário entre 0 e 23.")


# todo Ex 003

# nome = input('Digite seu nome: ')
# tamanho = len(nome)
#
# if tamanho <= 4:
#     print('Seu nome é curto.')
# elif tamanho <= 6:
#     print('Seu nome é normal.')
# else:
#     print('Seu nome é muito grande.')

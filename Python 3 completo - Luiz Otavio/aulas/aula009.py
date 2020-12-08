"""
    8.12.2020 - Felipe Ferreira de Aguiar
    Condições If, Else, Elif e Booleans
    Operadores relacionais == < <= > >= !=
    Operadores Logicos and, or, not, in, not in
"""
# ! Condições If, Else, Elif e Booleans

if True:
    print('Verdadeiro')

    num_1 = 2
    num_2 = 4
    print(num_1 + num_2)

elif False:
    print('Falso')

elif False:
    print('Ok')

else:
    print('Ok 2')

# ! Operadores relacionais == (Igual) < (menor) <=  > (maior) >= != (diferente)

num_1 = 2
num_2 = 2
teste = num_1 != num_2
print(teste)

# todo Desafio, uma pessoa so pode pegar um emprestimo se for maior de idade

nome = input('Qual o seu nome ? ')
idade = int(input('Quando voce nasceu ? ex: 1985 '))
renda = float(input('Qual a sua renda mensal ? '))
emprestimo = float(input('Qual seria o valor do emprestimo ? '))

maior_idade = 2020 - idade
credito = emprestimo / renda
credor = emprestimo * 1.23

if maior_idade >= 18 and idade < 70:
    print('')
    print('Ok voce é maior de 18 anos, vamos prosseguir com a analise')
    print('')
    print('=====Processando=====')
    print('======Analise Concluida======')
    if credito <= 0.3:
        print('')
        print(f'Parabens!!! {nome}')
        print(f'Seu emprestimo de BRL {emprestimo} foi liberado')
        print(f'Voce vai pagar um valor total de BRL {credor:.2f}')
        print('')
    if credito >= 0.3:
        print('')
        print(f'{nome} infelizmente seu credito foi negado, agradeçemos a preferencia')
        print('')   
else:
    print('')
    print('=====Processando=====')
    print('======Analise Concluida======')
    print(f'{nome} seu emprestimo não foi liberado, agradeçemos a preferencia')
    print('')
    
# ! Operadores Logicos and (e), or (ou), not (não), in, not in
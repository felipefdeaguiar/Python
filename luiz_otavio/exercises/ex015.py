"""
    23.12.2020 - Felipe Ferreira de Aguiar
    Estrutura de repetição While
"""

# ! Loop infinito "teste"
while True:
    nome = input('Qual o seu nome ? ')
    print(f'Seu nome é {nome} ! Ola')

# ! Estrutura de repeticação 0 à 99 "teste"
x = 0
while x < 100:
    print(x)
    x = x + 1

print('acabou')

# ! Estrutura dentro de outra estrutura while
x = 0
while x < 10:
    y = 0

    while y < 5:
        print(f'({x}),({y})')
        y = y + 1
    
    x = x + 1

print('acabou')

# ! Calculadora simples "teste"
while True:
    print()
    num_1 = input('Digite o primeiro numero inteiro ')
    num_2 = input('Digite o segundo numero inteiro ')
    operador = input('Digite o operador ')
    sair = input('Deseja sair ? [s] ou [n] ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Voce precisa digitar um valor correto')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # ? Operadores básicos! + , - , * , /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador Invalido')

   
    

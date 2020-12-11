"""
    10.12.2020 - Felipe Ferreira de Aguiar
    Quantidade de caracter
"""

# ! Validação quantidade de caracteres

usuario = input('Qual o seu nome ? ')
validacao = len(usuario)

if validacao < 6:
    print('Você precisa digitar no minimo seis caracteres')
else:
    print('Voce foi cadastrado')

# ! Somando duas strings e mosrando a quantidade de caracteres

string_1 = input('Digite alguma coisa : ')
string_2 = input('Digite outra coisa : ')

print(f'A quantidade total de caracteres digitado foi {len(string_1) + len(string_2)}')

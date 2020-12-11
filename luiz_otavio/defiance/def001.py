"""
    7.12.2020 - Felipe Ferreira de Aguiar
    Criar variaveis para nome (str), idade (int), altura (float), peso (float) de uma pessoa
    Criar uma variavel do ano atual (int), obter o ano de nascimento beseado no ano atual
    Fazer o calculo do IMC com duas casas decimais
    Exibir o texto com todos os valores na tela, usando o F-Strings com chave
"""

nome = 'Felipe Aguiar'
idade = 35
altura = 1.79
peso = 78.8
ano_atual = 2020
imc = peso / (altura ** 2)
ano_nascimento = 2020 - idade

print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')
print(f'seu IMC é {imc:.2f}, porque ele tem de altura {altura}M e {peso}Kg')

"""
    7.12.2020 - Felipe Ferreira de Aguiar
    Aula de formatação de strings
"""

nome = 'Felipe Aguiar'
idade = 35
altura = 1.79
peso = 78
maior_idade = idade > 18
imc = peso / (altura ** 2)

# ! Metodo I
print('Nome: {}\nIdade: {}\nAltura: {}\nÉ maior de Idade: {}'.format(nome, idade, altura, maior_idade))
print('Seu IMC é: {:.2f}'.format(imc))

# ! Metodo II
print(f'{nome} tem {idade} anos e seu IMC é {imc:.2f}')

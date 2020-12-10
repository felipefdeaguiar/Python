"""
    7.12.2020 - Felipe Ferreira de Aguiar
    Aula de variaveis
"""

# ! Atenção iniciar as variaveis semrpre com letra, pode conter numeros, separar com "_" e sempre letras minusculas

nome = 'Felipe Aguiar'
idade = 35
altura = 1.79
peso = 78
maior_idade = idade > 18
imc = peso / (altura ** 2)

print('Nome: {}\nIdade: {}\nAltura: {}\nÉ maior de Idade: {}'.format(nome, idade, altura, maior_idade))
print('Seu IMC é: {:.2f}'.format(imc))

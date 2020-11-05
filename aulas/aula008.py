"""
    curso Python 3 - Aula 008 - Utilizando Módulos
    Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.
    04.11.2020 - Felipe Ferreira de Aguiar
"""

#! from math import sqrt, outra forma de importar somente um modulo.
import math
num = int(input('Digite um numero inteiro '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#todo importar a biblioteca random e mostrar um numero inteiro aleatorio
import random
num = random.randint(1, 100)
print (num)

#todo desafio 016 - crie um programa que leia um numero real e mostre sua porção inteira
import math
real = float(input('Digite um numero real '))
conv = math.ceil(real)
print('O numero real digitado foi {} convertido para inteiro é {}'.format(real, conv))

#todo desafio 017 - crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo e calcule e mostre a sua hipotenusa
import math
cat_adj = float(input('Digite o valor do catero adjacente '))
cat_opt = float(input('Digite o valor do catero oposto '))
hipotenusa = math.hypot(cat_adj, cat_opt)
print('A hipotenusa é {:.2f}'.format(hipotenusa))

#todo desafio 018 - crie um programa que leia um angulo qualquer e mostre o valor do seno, cosseno e tangente
import math
ang = float(input('Digite qual é o angulo º '))
seno = math.sin(ang)
cons = math.cos(ang)
tang = math.tan(ang)
print('O angulo digitado foi {:.2f}, seu seno {:.2f}'.format(ang, seno), end='')
print(' seu cosseno {:.2f} e tangente {:.2f}'.format(cons, tang))

#todo desafio 019 - um professor quer sortear um dos seus alunos para apagar o quadro, faça um programa que leia os nomes dos quatro alunos e sortei um
import random
aluno_1 = str(input('Digite o nome do aluno 1 '))
aluno_2 = str(input('Digite o nome do aluno 2 '))
aluno_3 = str(input('Digite o nome do aluno 3 '))
aluno_4 = str(input('Digite o nome do aluno 4 '))
sort = random.choice([aluno_1, aluno_2, aluno_3, aluno_4])
print('O aluno {} foi o sorteado para apagar o quandro'.format(sort))

#todo desafio 020 - seguindo o mesmo conceito do desafio 017, agora o professor quer fazer um sorteio de ordem para uma apresentação
import random
aluno_1 = str(input('Digite o nome do aluno 1 '))
aluno_2 = str(input('Digite o nome do aluno 2 '))
aluno_3 = str(input('Digite o nome do aluno 3 '))
aluno_4 = str(input('Digite o nome do aluno 4 '))
sort = random.sample([aluno_1, aluno_2, aluno_3, aluno_4], k=4)
print('A apresentação será nessa ordem {}'.format(sort))

#todo desafio 021 - faça um programa que abra um arquivo MP3 e reproduza ou outros

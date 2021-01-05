"""
    06.01.2021 - Felipe Ferreira de Aguiar
    Estrutura de repetição While / Else (Contador / acumulador)
"""

# ! Estrutura simples de contador e acumulador
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador = contador + 1
else:
    print('acabei meus calculos')

# ! Estrutura simples de contador e acumulador (com um break dentro do laço)
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador = contador + 1

    if contador > 5:
        break

else:
    print('isso não será executado')

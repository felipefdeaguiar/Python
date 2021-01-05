contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador = contador + 1

    if contador > 5:
        break

else:
    print('acabei meus calculos')
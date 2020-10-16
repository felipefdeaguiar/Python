# -*- coding: utf-8 -*- 

import sys
operacao = input("Qual operação deseja fazer? ( * / - +)\n")

try:
    operando1 = float(input("Digite operando1:\n"))
    operando2 = float(input("Digite operando2:\n"))
except ValueError:
    print("Digite somente números nos operandos 1 e 2")
    sys.exit(1)

resultado = None
if operacao == "+":
    resultado = operando1 + operando2
elif operacao == "-":
    resultado = operando1 - operando2
elif operacao == "*":
    resultado = operando1 * operando2
elif operacao == "/" and operando2 == 0:
    print("Operação inválida: Divisão por 0")
    sys.exit(1)
elif operacao == "/":
    resultado = operando1 / operando2
else:
    print("Operação não existente!")

if resultado:
    print("Resultado: {0}".format(resultado))

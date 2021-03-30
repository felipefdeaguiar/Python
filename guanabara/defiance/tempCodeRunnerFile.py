num = input('Digite um valor de 0 à 9999 ')
if num.isdigit():
    print(f'\nO valor digitado foi {num}\nSua milhar é {num[0]}\nSua centena é {num[1]}\nSua dezena é {num[2]}\nSua unidade é {num[3]}\n')
else:
    print('Digite um valor correto')
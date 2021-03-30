name = input('Digite o nome da sua cidade natal ')
name_1 = name.split()
if 'Santo' in name_1[0]:
    print(f'\nA cidade digita foi "{name}" e ela começa por "Santo"\n')
else:
    print(f'\nA cidade digita foi "{name}" e ela não começa por "Santo\n')
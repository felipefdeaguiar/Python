"""
    10.12.2020 - Felipe Ferreira de Aguiar
    Projeto SetUp Car - V 1.0
"""

dt_budget = input('Qual a data de hoje DD/MM/AAAA: ')
nome_client = input('Digite o nome do cliente : ')
cpf_client = int(input('Digite o CPF do cliente (somente numeros): '))
marca_car = input('Qual a fabricante do veiculo: ')
model_car = input('Qual o modelo do veiculo: ')
ano_car = int(input('Qual o ano do modelo do veiculo: '))
fuel_car = int(input('Digite 0 para Etanol, 1 para Gasolina Premium ou 2 para Diesel: '))
whp_orig_car = float(input('Qual a potencia WHP aferiada no dinamômetro (Original): '))
kgmf_orig_car = float(input('Qual o Torque kgf. m aferiada no dinamômetro (Original): '))
turbo_car = int(input('Digite 1 para veiculo Turbo ou 0 para aspirado '))
kg_car = float(input('Qual o peso do veiculo em KG: '))
stage_car = int(input('Digite o nivel de stage do carro ( 1 , 2 ou 3 ): '))

# ! Resposta Padrão
def resposta():
    print('')
    print('Analisando Banco de Dados')
    print('')
    print('')
    print('================== Concluido ================== ')
    print('')
    print(f'A potencia estimada do {model_car} do cliente {nome_client} foi para {whp_md_car:.2f} Whp')
    print(f'O Torque estimado do {model_car} do cliente {nome_client} foi para {kgmf_md_car:.2f} kgf/m ')
    print(f'Parabéns {nome_client}')
    print('')
    print('========== Program By Felipe Aguiar =========== ')
    print('')

# ! Calculo Estimado para carro com Etanol, Turbo e Estagio 1
if fuel_car == 0 and turbo_car == 1 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.18
    kgmf_md_car = kgmf_orig_car * 1.10
    resposta()

# ! Calculo Estimado para carro com Etanol, Turbo e Estagio 2
if fuel_car == 0 and turbo_car == 1 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.36
    kgmf_md_car = kgmf_orig_car * 1.20
    resposta()

# ! Calculo Estimado para carro com Etanol, Turbo e Estagio 3
if fuel_car == 0 and turbo_car == 1 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.54
    kgmf_md_car = kgmf_orig_car * 1.30
    resposta()

# ! Calculo Estimado para carro com Etanol, Aspirado e Estagio 1
if fuel_car == 0 and turbo_car == 0 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.15
    kgmf_md_car = kgmf_orig_car * 1.07
    resposta()

# ! Calculo Estimado para carro com Etanol, Aspirado e Estagio 2
if fuel_car == 0 and turbo_car == 0 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.28
    kgmf_md_car = kgmf_orig_car * 1.13
    resposta()

# ! Calculo Estimado para carro com Etanol, Aspirado e Estagio 3
if fuel_car == 0 and turbo_car == 0 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.47
    kgmf_md_car = kgmf_orig_car * 1.22
    resposta()

# ! Calculo Estimado para carro com Gasolina, Turbo e Estagio 1
if fuel_car == 1 and turbo_car == 1 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.09
    kgmf_md_car = kgmf_orig_car * 1.07
    resposta()

# ! Calculo Estimado para carro com Gasolina, Turbo e Estagio 2
if fuel_car == 1 and turbo_car == 1 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.16
    kgmf_md_car = kgmf_orig_car * 1.12
    resposta()

# ! Calculo Estimado para carro com Gasolina, Turbo e Estagio 3
if fuel_car == 1 and turbo_car == 1 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.27
    kgmf_md_car = kgmf_orig_car * 1.20
    resposta()

# ! Calculo Estimado para carro com Gasolina, Aspirado e Estagio 1
if fuel_car == 1 and turbo_car == 0 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.06
    kgmf_md_car = kgmf_orig_car * 1.05
    resposta()

# ! Calculo Estimado para carro com Gasolina, Aspirado e Estagio 2
if fuel_car == 1 and turbo_car == 0 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.10
    kgmf_md_car = kgmf_orig_car * 1.08
    resposta()

# ! Calculo Estimado para carro com Gasolina, Aspirado e Estagio 3
if fuel_car == 1 and turbo_car == 0 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.17
    kgmf_md_car = kgmf_orig_car * 1.13
    resposta()

# ! Calculo Estimado para carro com Diesel, Turbo e Estagio 1
if fuel_car == 2 and turbo_car == 1 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.05
    kgmf_md_car = kgmf_orig_car * 1.20
    resposta()

# ! Calculo Estimado para carro com Diesel, Turbo e Estagio 2
if fuel_car == 2 and turbo_car == 1 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.11
    kgmf_md_car = kgmf_orig_car * 1.45
    resposta()

# ! Calculo Estimado para carro com Diesel, Turbo e Estagio 3
if fuel_car == 2 and turbo_car == 1 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.25
    kgmf_md_car = kgmf_orig_car * 1.101
    resposta()

# ! Calculo Estimado para carro com Diesel, Aspirado e Estagio 1
if fuel_car == 2 and turbo_car == 0 and stage_car == 1:
    whp_md_car = whp_orig_car * 1.04
    kgmf_md_car = kgmf_orig_car * 1.15
    resposta()

# ! Calculo Estimado para carro com Diesel, Aspirado e Estagio 2
if fuel_car == 2 and turbo_car == 0 and stage_car == 2:
    whp_md_car = whp_orig_car * 1.7
    kgmf_md_car = kgmf_orig_car * 1.28
    resposta()

# ! Calculo Estimado para carro com Diesel, Aspirado e Estagio 3
if fuel_car == 2 and turbo_car == 0 and stage_car == 3:
    whp_md_car = whp_orig_car * 1.13
    kgmf_md_car = kgmf_orig_car * 1.54
    resposta()
